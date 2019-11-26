from flask import Blueprint, jsonify
from flask_socketio import emit, join_room, leave_room
from flask import request
# from .viceController import ViceBoardController 
from . import socketio
import os
import json
# from xml.dom.minidom import parse, parseString
# import xml.etree.ElementTree as ET
import bs4 as bs
import glob



apirouter = Blueprint("router", __name__)
# myViceBoard = ViceBoardController()


@apirouter.route('/listAllConfigs',methods=['POST'])
def listAllConfigs():
  ## returns list of all existing config files
  cfiles = glob.glob('/Users/X-phile/Public/vicegui/backend/src/configFiles/*.xml')
  print('cfiles: ', cfiles)
  return jsonify({"cfiles": cfiles})


@apirouter.route('/getConfigParams',methods=['POST'])
def getConfigParams(selectedConfig):
  ## loads selected configuration file into dictionary of parameters
  ## returns dictionary of parameters to GUI

  configFile = open('./configFiles/testconfig.xml')
  # configFile = open(selectedConfig)
  soup = bs.BeautifulSoup(configFile, 'xml').prettify()
  paramlist = soup.find_all()

  paramdict = {}
  for i, plist in enumerate(paramlist):
    tag = plist[i].name
    val = plist[i].string
    print(tag, val)
    # check designated datatype, then convert
    paramdict.update( {tag:val} )

  return jsonify({'Parameters': paramdict})


@apirouter.route('/getConfigXML',methods=['POST'])
def getConfigXML(): #selectedConfig
  ## Parses contents of selected config file
  ## Passes prettified XML to GUI
  selectedConfig = str(request.get_json(force=True)['selected'])
  configFile = open(selectedConfig)
  soup = bs.BeautifulSoup(configFile, 'xml').prettify()
  return soup


@apirouter.route('/createNewConfig',methods=['POST'])
def createNewConfig():
  ## when "Submit" button is hit (either whole file editing // ind. parameter updates),
  ## creates new config file, names it with timestamp, and fills with updated configuration 
  return 0







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
