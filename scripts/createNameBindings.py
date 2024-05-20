import sys

fileName = sys.argv[0]
ServerID = sys.argv[1]
fp = open(fileName)
nameList=[]

#server = AdminConfig.getid(ServerID)
server = AdminConfig.getid(ServerID)

def printDic():
  print nameList

def getServerName(s):
    return AdminConfig.showAttribute(s, 'name')

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

def createList(fileRef):
  try:
    for line in fp:
      #print line,
      nameList.append(line)
  finally:
    fp.close()

# Add binding
def addBindingsToServer(s, newEntry):
    entry = newEntry.split('=:=')
    # Create binding
    print "Adding binding to Server %s" % getServerName(s)
    #print "AdminConfig.create('StringNameSpaceBinding', '%s', [['name', '%s'], ['nameInNameSpace', '%s'], ['stringToBind', '%s']])" % (s,entry[0],entry[1],entry[2].rstrip())
    print AdminConfig.create('StringNameSpaceBinding', s , [['name', entry[0]], ['nameInNameSpace', entry[1]], ['stringToBind', entry[2].rstrip()]])

def createNameBinding():
  for newEntry in nameList:
    print newEntry,
    addBindingsToServer(server, newEntry)

createList(fp)
#printDic()

createNameBinding()

saveConfig()
