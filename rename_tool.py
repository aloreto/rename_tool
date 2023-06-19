

'''
RENAME TOOL FOR MAYA

- Reanmes a list of selected objects based on string attributes.
- This predefined attributes are editable in the UI.
- It evaluates each item in the selection to see if is a "group" or a "geo" and renames it with the proper suffix.
_____________________________________________________________________________________________________________


SCRIPT TO LOAD THIS MODULE (TO BE RUN IN MAYA)
NOTE: I need to add the custom path because I use OneDrive. This resolves maya to no been able to see the documents
folder. Thus, it can not find the scripts folder and it fails to load the module.
The path has to be appended to maya paths.
_____________________________________________________________________________________________________________

import sys
sys.path.append('C:/Users/agust/OneDrive/01_TINTO/DOCUMENTS/maya/scripts/rename_tool')

import rename_tool

'''

import maya.cmds as cmds


# defining the variables for the name structure

obj_name = 'pepito'
sufix_group = 'grp'
sufix_geo = 'geo'
side = 'L'



# rename function

def renameObject(object, objectNewName):
    newlyRenamedObject=cmds.rename(object, objectNewName)


# loop evaluate and rename the list selection

def renameListOfObjects(selection):

    item_counter = 0

    for object in selection:

        object_shape = cmds.listRelatives(object, shapes=True)

        objectMesh = cmds.nodeType(object_shape)


        if objectMesh == 'mesh':


            meshObjectNewName = '{}_{}_{}_{}' .format( obj_name, item_counter, side, sufix_geo)

            renameObject(object, meshObjectNewName)

            item_counter = item_counter + 1


        else:

            groupObjectNewName = '{}_{}_{}_{}'.format(obj_name, item_counter, side, sufix_group)

            renameObject(object, groupObjectNewName)

            item_counter = item_counter + 1













