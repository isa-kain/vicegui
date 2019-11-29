from flask import Blueprint, jsonify
from flask_socketio import emit, join_room, leave_room
from flask import request
# from .viceController import ViceBoardController
from datetime import datetime 
from . import socketio
import os
import json
# from xml.dom.minidom import parse, parseString
import bs4 as bs
import glob



apirouter = Blueprint("router", __name__)
# myViceBoard = ViceBoardController()


@apirouter.route('/listAllConfigs',methods=['POST'])
def listAllConfigs():
  ## returns list of all existing config files
  cfiles = glob.glob('/Users/X-phile/Public/vicegui/backend/src/configFiles/*.xml')
  # for some reason, cfiles = cfiles.sort() returned null
  print('cfiles: ', cfiles)
  return jsonify({"cfiles": cfiles})


@apirouter.route('/getConfigParams',methods=['POST'])
def getConfigParams():
  ## loads selected configuration file into dictionary of parameters
  ## returns dictionary of parameters to GUI
  selectedConfig = request.get_json(force=True)['selectedConfig']
  # configFile = open('/Users/X-phile/Public/vicegui/backend/src/configFiles/dummy-config1.xml')
  configFile = open(selectedConfig)
  soup = bs.BeautifulSoup(configFile, 'xml') #only parses first couple of lines? wtf
  paramlist = soup.find_all()
  print('PARAM LIST: ', len(paramlist), paramlist)

  paramdict = {}
  for element in paramlist:
    if len(list(element.children))==1:
      tag = element.name
      val = element.string
      print(tag, val)
      paramdict.update( {tag:val} )

  return jsonify(paramdict)


@apirouter.route('/getConfigXML',methods=['POST'])
def getConfigXML(): #selectedConfig
  ## Parses contents of selected config file
  ## Passes prettified XML to GUI
  selectedConfig = str(request.get_json(force=True)['selected'])
  configFile = open(selectedConfig)
  soup = bs.BeautifulSoup(configFile, 'xml').prettify()
  configFile.close()
  return soup


@apirouter.route('/createNewConfig',methods=['POST'])
def createNewConfig(txt=None, newfilename=None):
  ## when "Submit" button is hit (either whole file editing // ind. parameter updates),
  ## creates new config file, names it with timestamp, and fills with updated configuration 
  timestamp = str(datetime.now()).replace(' ', '_')
  filepath = '/Users/X-phile/Public/vicegui/backend/src/configFiles/'

  try: newfilename = request.get_json(force=True)['newfilename']
  except: newfilename = None

  if newfilename is not None: newfile = open(filepath + timestamp + '_' + newfilename + '.xml', 'w+')
  else: newfile = open(filepath + timestamp + '.xml', 'w+')

  if txt==None: 
    txt = request.get_json(force=True)['changedConfig']
  print(txt)
  newfile.write(txt)
  newfile.close()
  return 'Writing complete: '+ timestamp


@apirouter.route('/updateConfigFromParams',methods=['POST'])
def updateConfigFromParams():
  ## recieves base configuration, dict of changes to that config from GUI
  ## writes changes in dict to text of config file
  ## writes new file by calling createNewConfig()

  basefile = request.get_json(force=True)['baseConfig']
  updates = request.get_json(force=True)['updates']
  newfilename = request.get_json(force=True)['newfilename']

  baseconfig = open(basefile)
  soup = bs.BeautifulSoup(baseconfig, 'xml')
  print(soup.prettify)

  # elementslist = soup.find_all()
  # for i, element in enumerate(elementslist):
  #   # print('Element: ', element, element.name, element.string)
  #   if element.name in updates.keys():
  #     print('Element: ', element.string, 'Matching update: ', updates[element.name])
  #     elementslist[i].string = updates[element.name]

  # for tag in soup.find_all():
  #   print(tag)
  #   if tag.name in updates.keys():
  #     tag.string = updates[tag.name]

  # print('SOUP: ', soup)


  for tag in soup.find_all():
    # print('TAG NAME BEFORE IF', tag.name, 'LEN CHILDREN', len(list(tag.children)))
    if len(list(tag.children))==1:
      if tag.name in updates.keys():
        # print('TAG NAME', tag.name)
        # print('TAG STRING', tag.string)
        tag.string = updates[tag.name]
      
  # print('SOUP: ', soup)

  # print('YAY IS UPDATED: ', soup.prettify())
  createNewConfig(txt=str(soup), newfilename=newfilename)

  return ''



## perhaps move to new API file when we start having functions that relate to the board?
def applyConfig():
  ## applies selected configuration to the board
  return ''







# @apirouter.route('/showChanges',methods=['POST'])
# def showChanges():
#   try:
#     message = 'Thing retrieved'
#     updatedParams = request.get_json(force=True)
#     print(updatedParams)
#     print(updatedParams['params'])
#     print(updatedParams['params']['selectClock'])

#   except Exception as e:
#     print('Error: ', e)
#     message = 'No can do'

#   if message=='No can do': return jsonify({"message": message})
#   else:
#     return jsonify({"data": request.data, 
#                     "query": request.query_string, 
#                     "args": request.args, 
#                     "json": request.get_json(force=True),
#                     "files": request.files,
#                     "values": request.values,
#                     "form": request.form,
#                     }) 
#                     ## request.data has raw data IF it could not be parsed.
#                     ## otherwise, parsed data in request.form, and data is empty
