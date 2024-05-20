# WebSphere-Jython-scripts
General jython scripts to work on WebSphere Command Line

### showNameBindings.py
ToRun: ``` /opt/IBM/WebSphereXX/AppServer/bin/wsadmin.sh -lang jython -f /tmp/showNameBindings.py```

### updateNameBindings.py

ToRun: ``` /opt/IBM/WebSphereXX/AppServer/bin/wsadmin.sh -lang jython -f updateNameBindings.py file <name,nameInNameSpace,stringToBind>```

>samples:
>name:
NAMESPACE/VALUE1/SUBVALUE/XXX=:=NEWVALUE

>nameInNameSpace:
NAMESPACE/VALUE1/SUBVALUE/XXX=:=NEWNAMESPACE/VALUE1/SUBVALUE/XXX

>stringToBind:
NAMESACE/VALUE1/SUBVALUE/PARAMAETER=:=NEWPARAMETERVALUE
```
 <namebindings:StringNameSpaceBinding xmi:id="StringNameSpaceBinding_123456789" name="VALUE" nameInNameSpace="NAMESPACE/VALUE1/SUBVALUE/XXX" stringToBind="dummy"/>
 <namebindings:StringNameSpaceBinding xmi:id="StringNameSpaceBinding_198726584" name="OLDPARAMETER" nameInNameSpace="NAMESACE/VALUE1/SUBVALUE/PARAMAETER" stringToBind="DUMMY"/>
```
