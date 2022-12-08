import pandas as pd
import subprocess



subprocess.run(["javac", "-classpath", "util/weka.jar", "util/MyWekaUtils.java", "A2.java"])
result = subprocess.check_output(["java", "-cp", ".:util/weka.jar", "A2", "features-timeslice-4.csv", "3"] + [str(i) for i in [1,4,5,9,11]], stderr=subprocess.STDOUT)
result = result.decode('utf-8')
print(result)