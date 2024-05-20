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
### updateNameBindingsSpecific.py

ToRun: ```/opt/IBM/WebSphereXX/AppServer/bin/wsadmin.sh -lang jython -f updateNameBindingsSpecific.py file <name,nameInNameSpace,stringToBind>```

>updateSpecificName.txt:
```
NAMESPACENA_AUTH_URL=:=NAMESPACE/WEBAUTH_URL=:=https://NAMESPACE.com
NAMESPACE_keyStoreFormat=:=NAMESPACE/CONFIG/keyStoreFormat=:=nCipher.sworld
NAMESPACE_keyStoreLocation=:=NAMESPACE/CONFIG/keyStoreLocation=:=/opt/NAMESPACE/keystore/config/name.keystore
NAMESPACE_keyStorePassword=:=NAMESPACE/CONFIG/keyStorePassword=:=password
NAMESPACE_keyStoreProvider=:=NAMESPACE/CONFIG/keyStoreProvider=:=nCipherKM
NAMESPACE_signingKeyAlias=:=NAMESPACE/CONFIG/signingKeyAlias=:=NEWPARAMETER
NAMESPACE_ExpiryTime=:=NAMESPACE/CONFIGExpiryTime=:=10
NAMESPACE_TOKEN_VALD_CERT_PATH=:=NAMESPACE/CONFIG/TOKEN_VALD_CERT_PATH=:=/opt/NAMESPACE/keystore/credential_encryption_sha256.cer
NAMESPACE_URL=:=NAMESPACE/URL=:=NEWURL
NAMESPACE_DEVICE_URL=:=NAMESPACE/DEVICE_URL=:=NEWURL
NAMESPACE_TRANS_URL=:=NAMESPACE/TRANS_URL=:=NEWURL
NAMESPACE_DSP-CONFIG_USER_PROFILE_URL=:=NAMESPACE/USER_PROFILE_URL=:=NEWURL
```
