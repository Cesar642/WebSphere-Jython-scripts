import sys

virtualHostParameter = sys.argv[0]

def printAllGeneralVirtualHost():
  virtualHosts=AdminConfig.list( "VirtualHost" ).splitlines()
  for vh in virtualHosts:
    print "%s: Aliases:%s" % (AdminConfig.showAttribute(vh, "name"), AdminConfig.showAttribute(vh, 'aliases'))
  #print "**%s" % type(virtualHosts)
  #print "=%s" % (AdminConfig.attributes("VirtualHost"))
  #print "-%s" % (AdminConfig.attributes("HostAlias"))

  for virtual in AdminConfig.list( "HostAlias" ).splitlines():
    print "%s->%s:%s" % (virtual,AdminConfig.showAttribute(virtual, "hostname"),AdminConfig.showAttribute(virtual, "port"))

def printPort():
  servers = AdminConfig.list( 'ServerEntry' ).splitlines()
  for server in servers :
    print '\n'
    print "Server Name : " +  server[0:server.find('(')]
    print "=" *30
    NamedEndPoints = AdminConfig.list( "NamedEndPoint" , server).splitlines()
    for namedEndPoint in NamedEndPoints:
        endPointName = AdminConfig.showAttribute(namedEndPoint, "endPointName" )
        endPoint = AdminConfig.showAttribute(namedEndPoint, "endPoint" )
        host = AdminConfig.showAttribute(endPoint, "host" )
        port = AdminConfig.showAttribute(endPoint, "port" )
        print "Endpoint Name  : " +  endPointName + " Host : " + host + " port : " + port

def editVirtualHost():
  print "Edit value"

def deleteVirtualHost():
  print "Delete value"


switcher = {
  1: editVirtualHost,
  2: deleteVirtualHost
}

def getOption(opcion):
  func = switcher.get(opcion, lambda: "Invalid option")
  print func()


def printSpecificVirtualHost(virtualHostParameter):
  virtualHosts=AdminConfig.list( "VirtualHost" ).splitlines()
  for vh in virtualHosts:
    print "AdminConfig.showAttribute(vh, \"name\"):%s,virtualHostParameter:%s" % (AdminConfig.showAttribute(vh, "name"),virtualHostParameter)
    if (AdminConfig.showAttribute(vh, "name") == virtualHostParameter):
      alias =  AdminConfig.showAttribute(vh, 'aliases')
      for aliasSplitted in alias.split(" "):
        for virtual in AdminConfig.list( "HostAlias" ).splitlines():
          #print "aliasSplitted:%s,virtual:%s" % (aliasSplitted,virtual)
          if (aliasSplitted.strip("[]")== virtual):
            print "%s->%s:%s" % (virtual,AdminConfig.showAttribute(virtual, "hostname"),AdminConfig.showAttribute(virtual, "port"))

            opcion = raw_input("Enter option:")
            getOption(opcion)

            break
      break

#printPort()
#printAllGeneralVirtualHost()
printSpecificVirtualHost(virtualHostParameter)
