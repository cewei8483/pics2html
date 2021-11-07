import os, base64, sys

picTypes = ('jpg', 'jpeg', 'png')

writePic = False
if len(sys.argv) > 1 and 'writePic' in sys.argv[1]:
    writePic = True

for dirPath, dirNames, fileNames in os.walk("."):
    print(f'{dirPath=} {dirNames=} {fileNames=}')
    fileNames = list(filter(lambda ele: ele.lower().endswith(picTypes), fileNames))
    if fileNames:
        htmlName = ''
        if dirPath == '.': # cwd
            htmlName = os.path.join(dirPath, os.path.basename(os.getcwd()))
        else: # subdirectory
            htmlName = os.path.join(dirPath, dirPath.split(os.path.sep)[-1])
        htmlName += '.html'
        print(f'{htmlName=}')
         
        with open(htmlName, "w", encoding='utf-8') as o:
            htmlContent = '''<!DOCTYPE html>
<html style="background-color:#999;">
<div style="text-align:center">
'''
            o.write(htmlContent)
            
            fileNames.sort()
            for f in fileNames:
                filePath = os.path.join(dirPath, f)
                
                data_uri = ''
                if writePic:
                    data_uri = base64.b64encode(open(filePath, 'rb').read()).decode('utf-8')
                    htmlContent = f'  <img style="display:block; margin:auto;" src="data:image/jpg;base64,{data_uri}">'
                else:
                    data_uri = f
                    htmlContent = f'  <img style="display:block; margin:auto;" src="{data_uri}">'
                    
                htmlContent += '\n'
                o.write(htmlContent)
            
            htmlContent = '''</div>
</html>'''
            o.write(htmlContent)
