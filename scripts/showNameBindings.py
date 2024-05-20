import sys

contentToFile=""
fileToWrite=open('NamesInBinding.out','w')

for ns in AdminConfig.list( 'NameSpaceBinding' ).splitlines() :
    name = AdminConfig.showAttribute( ns, 'name' )
    stringToBind = AdminConfig.showAttribute( ns, 'stringToBind' )
    nameInNameSpace = AdminConfig.showAttribute( ns, 'nameInNameSpace' )
    #print 'Name->%s=stringToBind->%s;nameInNameSpace->%s' % ( name, stringToBind, nameInNameSpace )
    contentToFile+=nameInNameSpace+ "=" + stringToBind + "\n"
        
    #print "--Complete line: %s" % (ns)
    #print '**Name->%s=stringToBind->%s;nameInNameSpace->%s' % ( name, stringToBind, nameInNameSpace )
    #contentToFile+="--Complete line: %s ** Name: %s ** stringToBind: %s ** nameInNameSpace: %s \n" % (ns, name, stringToBind, nameInNameSpace )


#print contentToFile
fileToWrite.write(contentToFile)
fileToWrite.close()
