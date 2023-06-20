

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

def renameListOfObjects(*args):

    selection = cmds.ls(sl=True)

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


def test():
    print 'test'





#_________________________________________________________________________________________

# --------------------------------------window ui------------------------------------------

#
renameTool_window = cmds.window()
cmds.columnLayout()
cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 100), (2, 250)] )
cmds.text( label='Name' )
name = cmds.textField()
cmds.text( label='sufix_geo')
sufix_geo_field = cmds.textField(text='geo' )
cmds.text( label='sufix_group' )
sufix_group_field = cmds.textField(text='grp' )
cmds.text( label='side' )
side_field = cmds.textField(text='C' )
cmds.setParent('..')

cmds.columnLayout()
cmds.button( label='Rename', command= renameListOfObjects, width = 350)
cmds.separator(h=30, width = 350)
cmds.text( label='Side suffix replacer', width=350, align= 'center' )
cmds.setParent('..')

cmds.rowColumnLayout( numberOfColumns=2, columnAttach=(1, 'right', 0), columnWidth=[(1, 175), (2, 175)] )
currentLetterField= cmds.textField()
cmds.text( label='current side letter')
cmds.setParent('..')

cmds.columnLayout()
cmds.button( label='Rename Side Letter', command= test, width = 350)
cmds.setParent('..')


cmds.showWindow( renameTool_window )












