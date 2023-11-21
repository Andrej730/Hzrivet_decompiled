# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)]
# Embedded file name: C:/Users/qeeji/Documents/maya/2015-x64/scripts\HZrivet\nodes.py
# Compiled at: 2011-03-20 11:35:28
"""
file -> file:node.py
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
import maya.cmds as cmd

def nRivet(input, UVs):
    pOSI = cmd.createNode('pointOnSurfaceInfo', n=input.split('.')[0] + '_pOSI')
    cmd.setAttr('.turnOnPercentage', 1)
    rivet = cmd.spaceLocator(n=input.split('.')[0] + '_nRivet')
    cmd.addAttr(ln='HZrivet', at='enum', en='_________:')
    cmd.addAttr(ln='U', at='double', min=0, max=1, dv=UVs[0])
    cmd.addAttr(ln='V', at='double', min=0, max=1, dv=UVs[1])
    cmd.setAttr('.HZrivet', l=1, k=0, cb=1)
    cmd.setAttr('.U', l=0, k=1)
    cmd.setAttr('.V', l=0, k=1)
    aim = cmd.createNode('aimConstraint', n=input.split('.')[0] + '_aC', p=rivet[0])
    cmd.connectAttr(input, pOSI + '.inputSurface', f=1)
    cmd.connectAttr(pOSI + '.normal', aim + '.target[0].targetTranslate', f=1)
    cmd.connectAttr(pOSI + '.tangentV', aim + '.worldUpVector', f=1)
    cmd.connectAttr(aim + '.constraintRotate', rivet[0] + '.rotate', f=1)
    cmd.connectAttr(pOSI + '.position', rivet[0] + '.translate', f=1)
    cmd.connectAttr(rivet[0] + '.U', pOSI + '.parameterU', f=1)
    cmd.connectAttr(rivet[0] + '.V', pOSI + '.parameterV', f=1)
    return rivet[0]


def pRivet(input, infos):
    edge_1 = cmd.createNode('curveFromMeshEdge', n=input.split('.')[0] + '_curveFromEdge_1_')
    edge_2 = cmd.createNode('curveFromMeshEdge', n=input.split('.')[0] + '_curveFromEdge_2_')
    loft = cmd.createNode('loft', n=input.split('.')[0] + '_loft')
    output = loft + '.outputSurface'
    max = cmd.polyEvaluate(input.split('.')[0], e=1)
    cmd.connectAttr(input, edge_1 + '.inputMesh', f=1)
    cmd.connectAttr(input, edge_2 + '.inputMesh', f=1)
    cmd.connectAttr(edge_1 + '.outputCurve', loft + '.inputCurve[0]', f=1)
    cmd.connectAttr(edge_2 + '.outputCurve', loft + '.inputCurve[1]', f=1)
    pOSI = cmd.createNode('pointOnSurfaceInfo', n=input.split('.')[0] + '_pOSI')
    cmd.setAttr('.turnOnPercentage', 1)
    rivet = cmd.spaceLocator(n=input.split('.')[0] + '_pRivet')
    cmd.addAttr(ln='HZrivet', at='enum', en='_________:')
    cmd.addAttr(ln='U', at='double', min=0, max=1, dv=infos[0])
    cmd.addAttr(ln='V', at='double', min=0, max=1, dv=infos[1])
    cmd.addAttr(ln='edge_1_index', at='long', min=0, max=max, dv=infos[2])
    cmd.addAttr(ln='edge_2_index', at='long', min=0, max=max, dv=infos[3])
    cmd.setAttr('.HZrivet', l=1, k=0, cb=1)
    cmd.setAttr('.U', l=0, k=1)
    cmd.setAttr('.V', l=0, k=1)
    cmd.setAttr('.edge_1_index', l=0, k=1)
    cmd.setAttr('.edge_2_index', l=0, k=1)
    aim = cmd.createNode('aimConstraint', n=input.split('.')[0] + '_aC', p=rivet[0])
    cmd.connectAttr(output, pOSI + '.inputSurface', f=1)
    cmd.connectAttr(pOSI + '.normal', aim + '.target[0].targetTranslate', f=1)
    cmd.connectAttr(pOSI + '.tangentV', aim + '.worldUpVector', f=1)
    cmd.connectAttr(aim + '.constraintRotate', rivet[0] + '.rotate', f=1)
    cmd.connectAttr(pOSI + '.position', rivet[0] + '.translate', f=1)
    cmd.connectAttr(rivet[0] + '.U', pOSI + '.parameterU', f=1)
    cmd.connectAttr(rivet[0] + '.V', pOSI + '.parameterV', f=1)
    cmd.connectAttr(rivet[0] + '.edge_1_index', edge_1 + '.edgeIndex[0]', f=1)
    cmd.connectAttr(rivet[0] + '.edge_2_index', edge_2 + '.edgeIndex[0]', f=1)
    return rivet[0]