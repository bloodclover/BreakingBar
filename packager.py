# All this to avoid the old version warning btw
# Also, yall windows users aint gettin' any of this

import os
import subprocess

# Some checks
if os.getcwd() != os.path.dirname(os.path.realpath(__file__)):
        print("Please run the program in its working directory")
        exit(1)

print("Started the resourcepack zipper!")

supported_formats = [
[1, "1.6.1_1.8.9"],
[2, "1.9_1.10.2"], 
[3, "1.11_1.12.2"], 
[4, "1.13_1.14.4"], 
[5, "1.15_1.16.1"], 
[6, "1.16.2_1.16.5"], 
[7, "1.17_1.17.1"], 
[8, "1.18_1.18.2"], 
[9, "1.19_1.19.2"], 
[12, "1.19.3"], 
[13, "1.19.4"], 
[15, "1.20_1.20.1"], 
[18, "1.20.2"], 
[22, "1.20.3_1.20.4"], 
[32, "1.20.5_1.20.6"], 
[34, "1.21_1.21.1"], 
[42, "1.21.2_1.21.3"], 
[46, "1.21.4"], 
[55, "1.21.5"], 
[63, "1.21.6"], 
[64, "1.21.7_1.21.8"], 
[69, "1.21.9_1.21.10"], 
[75, "1.21.11"], 
[84, "26.1_26.1.2"], 
[88, "26.2"]
]

print("Initializing")
if os.path.exists("./packs"):
       input = input("There already is a packs folder, do you want to override it? [y/N]")
       if not input.lower() == "y":
              print("Cancelled operation")
              exit()

       subprocess.run("rm -r packs", shell=True)

if os.path.exists("./tmp"):
       subprocess.run("rm -r tmp", shell=True)

subprocess.run("mkdir packs", shell=True)


print("Compiling Resourcepacks")
for format, mcVer in supported_formats:
    packmeta = """{"pack": {"description": "A loading bar like breaking animation","pack_format": """ + str(format) + """}}"""
    filename = f"{mcVer}__{str(format)}"
    subprocess.run("mkdir tmp", shell=True)
    subprocess.run("cp -r ./assets ./tmp", shell=True)
    subprocess.run("cp ./LICENSE ./tmp", shell=True)
    subprocess.run("cp ./pack.png ./tmp", shell=True)

    mcmeta = open("./tmp/pack.mcmeta", "x")
    mcmeta.write(packmeta)
    mcmeta.close()

    if format < 4:
            subprocess.run("rm -r ./tmp/assets/minecraft/textures/block", shell=True)
    else:
            subprocess.run("rm -r ./tmp/assets/minecraft/textures/blocks", shell=True)
    subprocess.run(f"mkdir ./packs/{filename}", shell=True)
    subprocess.run(f"cp -r ./tmp/* ./packs/{filename}", shell=True)
    subprocess.run("rm -r ./tmp", shell=True)
    os.chdir(f"./packs/{filename}")
    subprocess.run(f"zip -rq9 ./BreakingBar.zip ./*", shell=True)
    os.chdir("../..")

    print("Completed " + filename)

print("Done!")
