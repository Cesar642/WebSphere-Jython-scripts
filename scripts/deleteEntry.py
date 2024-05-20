import sys

fileName = sys.argv[0]
whatToDelete = sys.argv[1]

nameDic={}
#fp = open("NamesInBinding.out")
fp = open(fileName)

def createdic(fileRef):
  try:
    for line in fileRef:
      #print line,
      lineSplit = line.split('\n')[0]
      nameDic[lineSplit]=lineSplit
  finally:
    fileRef.close()

def printDic():
  print nameDic

def findKey(key):
  exist = False
  if key in nameDic:
    print "key %s found with value %s" % (key, nameDic[key])
    exist = True
  return exist

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

def deleteKey(toDelete):
  for ns in AdminConfig.list( toDelete ).splitlines() :
    name = AdminConfig.showAttribute( ns, 'name' )
    if (findKey(name)):
	  print "Delete %s" % name
	  AdminConfig.remove(ns)

createdic(fp)

printDic()

deleteKey(whatToDelete)

saveConfig()
