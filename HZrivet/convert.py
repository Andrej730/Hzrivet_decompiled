# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:19:08) [MSC v.1500 32 bit (Intel)]
# Embedded file name: C:/Users/qeeji/Documents/maya/2015-x64/scripts\HZrivet\convert.py
# Compiled at: 2011-03-20 11:35:00
"""
file -> file:convert.py
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

def calculation(uN, vN, value=(0.5, 0)):
    U = []
    V = []
    final = []
    if uN == 1:
        if value[1] == 0:
            U.append(value[0])
        elif value[1] == 1:
            U.append(value[0])
        else:
            U.append(0.5)
    else:
        start = 0.0
        while start <= 1.0:
            U.append(start)
            start += 1.0 / (uN - 1)

        if vN == 1:
            if value[1] == 0:
                V.append(value[0])
            elif value[1] == 1:
                V.append(0.5)
            else:
                V.append(value[0])
        else:
            start = 0.0
            while start <= 1.0:
                V.append(start)
                start += 1.0 / (vN - 1)

        for varU in U:
            for varV in V:
                final.append((varU, varV))

    return final


def vetexToEdgeIndexes(vetex):
    toEdges = cmd.ls(cmd.polyListComponentConversion(vetex, fv=1, te=1), fl=1)
    return (int(toEdges[0].split(']')[0].split('[')[1]), int(toEdges[1].split(']')[0].split('[')[1]))


def faceToEdgeIndexes(face):
    toEdges = cmd.ls(cmd.polyListComponentConversion(face, ff=1, te=1), fl=1)
    if len(toEdges) > 2:
        fistEdgeToVtxs = cmd.ls(cmd.polyListComponentConversion(toEdges[0], fe=1, tv=1), fl=1)
        if len(toEdges) == 3:
            return (int(toEdges[0].split(']')[0].split('[')[1]), int(toEdges[1].split(']')[0].split('[')[1]))
        if len(toEdges) > 3:
            for var in toEdges:
                tmpFdgeToVtxs = cmd.ls(cmd.polyListComponentConversion(var, fe=1, tv=1), fl=1)
                if tmpFdgeToVtxs[0] not in fistEdgeToVtxs and tmpFdgeToVtxs[1] not in fistEdgeToVtxs:
                    return (
                     int(toEdges[0].split(']')[0].split('[')[1]), int(var.split(']')[0].split('[')[1]))
                    break

    else:
        return
    return


def meshToPerFace(mesh):
    final = []
    numFs = cmd.polyEvaluate(mesh, f=1)
    for i in range(0, numFs):
        if cmd.objExists(mesh + '.f[' + str(i) + ']'):
            child = faceToEdgeIndexes(mesh + '.f[' + str(i) + ']')
            if child is not None:
                final.append(child)

    return final


def getFromMaya(uN, vN):
    sels = cmd.ls(sl=1, fl=1)
    final = []
    i = 0
    while i < len(sels):
        if cmd.nodeType(sels[i]) == 'transform':
            shapes = cmd.listRelatives(sels[i], s=1)
            if len(shapes) > 0:
                for shape in shapes:
                    if cmd.nodeType(shape) == 'nurbsSurface':
                        gets = calculation(uN, vN)
                        for each in gets:
                            final.append((shape + '.ws[0]', each))

                    elif cmd.nodeType(shape) == 'mesh':
                        allIndexes = meshToPerFace(shape)
                        gets = calculation(uN, vN)
                        for perIndex in allIndexes:
                            for each in gets:
                                final.append((shape + '.worldMesh[0]', (each[0], each[1], perIndex[0], perIndex[1])))

                    else:
                        print shape + 'is out of HZrivet basic object\n'

                i += 1
            else:
                i += 1
                print sels[i] + 'is out of HZrivet basic object\n'
        elif cmd.nodeType(sels[i]) == 'nurbsSurface':
            if '.' in sels[i]:
                if '.u[' in sels[i]:
                    value = float(sels[i].split(']')[0].split('[')[1]) / cmd.getAttr(sels[i].split('.')[0] + '.mmu')[0][1]
                    gets = calculation(1, vN, (value, 1))
                    for each in gets:
                        final.append((sels[i].split('.')[0] + '.ws[0]', each))

                    i += 1
                elif '.v[' in sels[i]:
                    value = float(sels[i].split(']')[0].split('[')[1]) / cmd.getAttr(sels[i].split('.')[0] + '.mmv')[0][1]
                    gets = calculation(uN, 1, (value, 2))
                    for each in gets:
                        final.append((sels[i].split('.')[0] + '.ws[0]', each))

                    i += 1
                elif '.uv[' in sels[i]:
                    uV = float(sels[i].split(']')[0].split('[')[1]) / cmd.getAttr(sels[i].split('.')[0] + '.mmu')[0][1]
                    vV = float(sels[i].split(']')[1].split('[')[1]) / cmd.getAttr(sels[i].split('.')[0] + '.mmv')[0][1]
                    final.append((sels[i].split('.')[0] + '.ws[0]', (uV, vV)))
                    i += 1
                else:
                    i += 1
                    print sels[i] + 'is out of HZrivet basic object\n'
            else:
                gets = calculation(uN, vN)
                for each in gets:
                    final.append((sels[i] + '.ws[0]', each))

                i += 1
        elif cmd.nodeType(sels[i]) == 'mesh':
            if '.' in sels[i]:
                if 'f[' in sels[i]:
                    indexes = faceToEdgeIndexes(sels[i])
                    if indexes is not None:
                        gets = calculation(uN, vN)
                        for each in gets:
                            final.append((sels[i].split('.')[0] + '.worldMesh[0]', (each[0], each[1], indexes[0], indexes[1])))

                    i += 1
                elif 'e[' in sels[i]:
                    if 'e[' in sels[(i + 1)]:
                        index_1 = int(sels[i].split(']')[0].split('[')[1])
                        index_2 = int(sels[(i + 1)].split(']')[0].split('[')[1])
                        gets = calculation(uN, vN)
                        for each in gets:
                            final.append((sels[i].split('.')[0] + '.worldMesh[0]', (each[0], each[1], index_1, index_2)))

                        i += 2
                    else:
                        print '"' + sels[i] + '" to "' + sels[(i + 1)] + '" you need select double mesh edges in order,or this scrip can\'t find out what you need'
                        i += 1
                elif 'vtx[' in sels[i]:
                    indexes = vetexToEdgeIndexes(sels[i])
                    final.append((sels[i].split('.')[0] + '.worldMesh[0]', (0.0, 0.0, indexes[0], indexes[1]), sels[i]))
                    i += 1
                else:
                    i += 1
                    print sels[i] + 'is out of HZrivet basic object\n'
            else:
                allIndexes = meshToPerFace(sels[i])
                gets = calculation(uN, vN)
                for perIndex in allIndexes:
                    for each in gets:
                        final.append((shape + '.worldMesh[0]', (each[0], each[1], perIndex[0], perIndex[1])))

                i += 1
        else:
            i += 1
            print sels[i] + 'is out of HZrivet basic object\n'

    return final