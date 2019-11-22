from flask import Blueprint, jsonify
from flask_socketio import emit, join_room, leave_room
from flask import request
# from .viceController import ViceBoardController 
from . import socketio
import os
import json
# from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET


apirouter = Blueprint("router", __name__)
# myViceBoard = ViceBoardController()

@apirouter.route('/sayHello',methods=['GET'])
def sayHello():
  try:
    message = 'Hello!'

  except Exception as e:
    print('Error: ', e)
    message = 'No hello'
  return jsonify({"message": message})


@apirouter.route('/showChanges',methods=['POST'])
def showChanges():
  try:
    message = 'Thing retrieved'
    updatedParams = request.get_json(force=True)
    print(updatedParams)
    print(updatedParams['params'])
    print(updatedParams['params']['selectClock'])

  except Exception as e:
    print('Error: ', e)
    message = 'No can do'

  if message=='No can do': return jsonify({"message": message})
  else:
    return jsonify({"data": request.data, 
                    "query": request.query_string, 
                    "args": request.args, 
                    "json": request.get_json(force=True),
                    "files": request.files,
                    "values": request.values,
                    "form": request.form,
                    }) 
                    ## request.data has raw data IF it could not be parsed.
                    ## otherwise, parsed data in request.form, and data is empty


# XML parsing uses ElementTree API:
# https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree

def updateConfiguration(updatesFromGui):
  ## loads configuration file into editable format
  configTree = ET.parse('testconfig.xml') #tree represents whole XML document
  configRoot = configTree.getroot() #root represents body of data n file
  # root divided into children, each of which have attributes:
    # tag; attribute; 
  # for param in root.findall('targetParameter'):




  # print(configData) ## Document instance, print doesn't show contents
  ## writes changes onto configuration file
    ## for each key in updates (which is a json object):
      ## find corresponding section in configFile
      ## write new value to that section
  ## sends updated file back to wherever we're keeping the configuration
  ## some way to inform system that an update has occurred?
  ## we can do version control like with H4GUI, and/or keep a file header that contains date&time of last change
  return 0



