# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)]
# Embedded file name: C:/Users/qeeji/Documents/maya/2015-x64/scripts\HZrivet\UI.py
# Compiled at: 2011-03-20 11:35:52
"""
file -> file UI.py
funtions -> 

++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++
author: John HuangZhen
date: 20110320

contact me:
        http://qeeji.weebly.com/(personal website)
        qeejihz@gmail.com
        qeeji@hotmaol.com
        
All Rights Reserved
"""
import maya.cmds as cmd, HZrivet.convert as convert, HZrivet.nodes as nodes

def UI():
    if cmd.window('HZrivet_mainWin', q=1, ex=1):
        cmd.deleteUI('HZrivet_mainWin')
    window = cmd.window('HZrivet_mainWin', title='HZrivet', mxb=0, tbm=0)
    cmd.columnLayout(adj=1)
    cmd.rowColumnLayout(nc=4, cw=[(1, 30), (2, 60), (3, 30), (4, 60)])
    cmd.text(l='  U:')
    cmd.intField('HZrivet_uNum', min=1, v=1)
    cmd.text(l='  V:')
    cmd.intField('HZrivet_vNum', min=1, v=1)
    cmd.setParent('..')
    cmd.separator(h=10)
    cmd.rowColumnLayout(nc=2, cw=[(1, 90), (2, 90)])
    cmd.button(l='create', h=50, c='HZrivet.UI.HZrivet_finalCC()')
    cmd.button(l='close', h=50, c='import maya.cmds as cmd;cmd.deleteUI("HZrivet_mainWin")')
    cmd.setParent('..')
    cmd.window('HZrivet_mainWin', e=1, widthHeight=(188, 112))
    cmd.showWindow('HZrivet_mainWin')


def HZrivet_finalCC():
    uN = cmd.intField('HZrivet_uNum', q=1, v=1)
    vN = cmd.intField('HZrivet_vNum', q=1, v=1)
    infos = convert.getFromMaya(uN, vN)
    for info in infos:
        if len(info[1]) == 2:
            rivet = nodes.nRivet(info[0], info[1])
        else:
            rivet = nodes.pRivet(info[0], info[1])
            if len(info) == 3:
                pos_1 = cmd.pointPosition(info[2])
                pos_2 = cmd.getAttr(rivet + '.wp')
                if abs(pos_1[0] - pos_2[0][0]) > 0.001 or abs(pos_1[1] - pos_2[0][1]) > 0.001 or abs(pos_1[2] - pos_2[0][2]) > 0.001:
                    cmd.setAttr(rivet + '.U', 1.0)
                    cmd.setAttr(rivet + '.V', 1.0)