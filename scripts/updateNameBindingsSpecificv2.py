import sys

fileName = sys.argv[0]
whatToUpdate = sys.argv[1]
applicationName = sys.argv[2]

nameDic={}
#fp = open("NamesInBinding.out")
fp = open(fileName)

def createdic(fileRef):
  try:
    for line in fp:
      #print line,
      lineSplit = line.split('=:=')
      nameDic[lineSplit[0]]=lineSplit[1].split('\n')[0]
  finally:
    fp.close()

def printDic():
  print nameDic

def findKey(key):
  exist = False
  if key in nameDic:
    print "key %s found with value %s" % (key, nameDic[key])
    exist = True
  return exist

def updateValuesInConfig(typeToEdit, params):
  #print "Update typeToEdit %s, params %s" % (typeToEdit, params)
  print "#AdminConfig.modify(%s, %s)" % (typeToEdit, params)
  print AdminConfig.modify(typeToEdit, params)

def saveConfig():
  print "Saving..."
  AdminConfig.save()
  print "All changes saved"
  syncNodes()

def syncNodes():
  # Obtain deployment manager MBean
  dm=AdminControl.queryNames("type=DeploymentManager,*")

  # "syncActiveNodes" can only be run on the deployment manager's MBean,
  # it will fail in standalone environment
  if dm:
    print "Synchronizing configuration repository with nodes. Please wait..."
    # Force sync with all currently active nodes
    nodes=AdminControl.invoke(dm, "syncActiveNodes", "true")
    print "The following nodes have been synchronized: "+str(nodes)
  else:
    print "Standalone server, no nodes to sync"

def updateKeys(toUpdate):
  for ns in AdminConfig.list( 'NameSpaceBinding','*' + applicationName +  '*' ).splitlines() :
    name = AdminConfig.showAttribute( ns, 'name' )
    stringToBind = AdminConfig.showAttribute( ns, 'stringToBind' )
    nameInNameSpace = AdminConfig.showAttribute( ns, 'nameInNameSpace' )
    #print "**nameInNameSpace: %s\n" % (nameInNameSpace)
    #print "**ns: %s\n" % (ns)
    if (findKey(nameInNameSpace)):
    #if (findKey(ns)):
      if (whatToUpdate == "stringToBind"):
        print "Update stringToBind"
        params = "[[name " + name + "] [nameInNameSpace " + nameInNameSpace + "] [stringToBind " + nameDic[nameInNameSpace] + "]]"
      elif (whatToUpdate == "nameInNameSpace"):
        print "Update nameInNameSpace"
        params = "[[name " + name + "] [nameInNameSpace " + nameDic[nameInNameSpace] + "] [stringToBind " + stringToBind + "]]"
      elif (whatToUpdate == "name"):
        print "Update name"
        params = "[[name " + nameDic[nameInNameSpace] + "] [nameInNameSpace " + nameInNameSpace + "] [stringToBind " + stringToBind + "]]"
      typeToEdit = ns
      #updateValuesInConfig(typeToEdit, params)
      print "AdminConfig.modify(%s, %s)" % (typeToEdit, params)
      print AdminConfig.modify(typeToEdit, params)

#findKey("HSBC/SECF/GLOBAL/CONFIGMANAGER/CONFIG/externalConfig")

createdic(fp)

#printDic()

updateKeys(whatToUpdate)

saveConfig()
