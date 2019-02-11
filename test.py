from src.Colors import TextColor

import os
import subprocess as subproc

stringNameOfAPK = "FindNumbers"

payloadsBaseDir = os.getcwd() + "/CreateMalware/android/codeinjection/payloads"
pathToNewApk = '/home/topcoder/Desktop/output'

stringJarSignerCommand = ["jarsigner", "-verbose", "-sigalg", "SHA1withRSA", "-digestalg", "SHA1", "-keystore",
                          payloadsBaseDir + "/fhackKey.keystore", "-storepass", "123456",
                          str(pathToNewApk) + "/" + stringNameOfAPK + '.apk', "alias_name"]
print TextColor.WARNING + "[*] wait to signeing application ..." + TextColor.WHITE
p = subproc.Popen(stringJarSignerCommand, stdout=subproc.PIPE)
jarsignerResult = p.communicate()[0]


print jarsignerResult