"""Automatically generated by binding_generator.py.

MuJoCo header version: 150
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import collections
# pylint: disable=invalid-name
# pylint: disable=line-too-long

# ------------------------------------Enums------------------------------------

mjtWarning = collections.namedtuple(
    "mjtWarning",
    ["mjWARN_INERTIA",
     "mjWARN_CONTACTFULL",
     "mjWARN_CNSTRFULL",
     "mjWARN_VGEOMFULL",
     "mjWARN_BADQPOS",
     "mjWARN_BADQVEL",
     "mjWARN_BADQACC",
     "mjWARN_BADCTRL",
     "mjNWARNING"]
)(0, 1, 2, 3, 4, 5, 6, 7, 8)

mjtTimer = collections.namedtuple(
    "mjtTimer",
    ["mjTIMER_STEP",
     "mjTIMER_FORWARD",
     "mjTIMER_INVERSE",
     "mjTIMER_POSITION",
     "mjTIMER_VELOCITY",
     "mjTIMER_ACTUATION",
     "mjTIMER_ACCELERATION",
     "mjTIMER_CONSTRAINT",
     "mjTIMER_POS_KINEMATICS",
     "mjTIMER_POS_INERTIA",
     "mjTIMER_POS_COLLISION",
     "mjTIMER_POS_MAKE",
     "mjTIMER_POS_PROJECT",
     "mjNTIMER"]
)(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

mjtDisableBit = collections.namedtuple(
    "mjtDisableBit",
    ["mjDSBL_CONSTRAINT",
     "mjDSBL_EQUALITY",
     "mjDSBL_FRICTIONLOSS",
     "mjDSBL_LIMIT",
     "mjDSBL_CONTACT",
     "mjDSBL_PASSIVE",
     "mjDSBL_GRAVITY",
     "mjDSBL_CLAMPCTRL",
     "mjDSBL_WARMSTART",
     "mjDSBL_FILTERPARENT",
     "mjDSBL_ACTUATION",
     "mjDSBL_REFSAFE",
     "mjNDISABLE"]
)(1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 12)

mjtEnableBit = collections.namedtuple(
    "mjtEnableBit",
    ["mjENBL_OVERRIDE",
     "mjENBL_ENERGY",
     "mjENBL_FWDINV",
     "mjENBL_SENSORNOISE",
     "mjNENABLE"]
)(1, 2, 4, 8, 4)

mjtJoint = collections.namedtuple(
    "mjtJoint",
    ["mjJNT_FREE",
     "mjJNT_BALL",
     "mjJNT_SLIDE",
     "mjJNT_HINGE"]
)(0, 1, 2, 3)

mjtGeom = collections.namedtuple(
    "mjtGeom",
    ["mjGEOM_PLANE",
     "mjGEOM_HFIELD",
     "mjGEOM_SPHERE",
     "mjGEOM_CAPSULE",
     "mjGEOM_ELLIPSOID",
     "mjGEOM_CYLINDER",
     "mjGEOM_BOX",
     "mjGEOM_MESH",
     "mjNGEOMTYPES",
     "mjGEOM_ARROW",
     "mjGEOM_ARROW1",
     "mjGEOM_ARROW2",
     "mjGEOM_LABEL",
     "mjGEOM_NONE"]
)(0, 1, 2, 3, 4, 5, 6, 7, 8, 100, 101, 102, 103, 1001)

mjtCamLight = collections.namedtuple(
    "mjtCamLight",
    ["mjCAMLIGHT_FIXED",
     "mjCAMLIGHT_TRACK",
     "mjCAMLIGHT_TRACKCOM",
     "mjCAMLIGHT_TARGETBODY",
     "mjCAMLIGHT_TARGETBODYCOM"]
)(0, 1, 2, 3, 4)

mjtTexture = collections.namedtuple(
    "mjtTexture",
    ["mjTEXTURE_2D",
     "mjTEXTURE_CUBE",
     "mjTEXTURE_SKYBOX"]
)(0, 1, 2)

mjtIntegrator = collections.namedtuple(
    "mjtIntegrator",
    ["mjINT_EULER",
     "mjINT_RK4"]
)(0, 1)

mjtCollision = collections.namedtuple(
    "mjtCollision",
    ["mjCOL_ALL",
     "mjCOL_PAIR",
     "mjCOL_DYNAMIC"]
)(0, 1, 2)

mjtCone = collections.namedtuple(
    "mjtCone",
    ["mjCONE_PYRAMIDAL",
     "mjCONE_ELLIPTIC"]
)(0, 1)

mjtJacobian = collections.namedtuple(
    "mjtJacobian",
    ["mjJAC_DENSE",
     "mjJAC_SPARSE",
     "mjJAC_AUTO"]
)(0, 1, 2)

mjtSolver = collections.namedtuple(
    "mjtSolver",
    ["mjSOL_PGS",
     "mjSOL_CG",
     "mjSOL_NEWTON"]
)(0, 1, 2)

mjtImp = collections.namedtuple(
    "mjtImp",
    ["mjIMP_CONSTANT",
     "mjIMP_SIGMOID",
     "mjIMP_LINEAR",
     "mjIMP_USER"]
)(0, 1, 2, 3)

mjtRef = collections.namedtuple(
    "mjtRef",
    ["mjREF_SPRING",
     "mjREF_USER"]
)(0, 1)

mjtEq = collections.namedtuple(
    "mjtEq",
    ["mjEQ_CONNECT",
     "mjEQ_WELD",
     "mjEQ_JOINT",
     "mjEQ_TENDON",
     "mjEQ_DISTANCE"]
)(0, 1, 2, 3, 4)

mjtWrap = collections.namedtuple(
    "mjtWrap",
    ["mjWRAP_NONE",
     "mjWRAP_JOINT",
     "mjWRAP_PULLEY",
     "mjWRAP_SITE",
     "mjWRAP_SPHERE",
     "mjWRAP_CYLINDER"]
)(0, 1, 2, 3, 4, 5)

mjtTrn = collections.namedtuple(
    "mjtTrn",
    ["mjTRN_JOINT",
     "mjTRN_JOINTINPARENT",
     "mjTRN_SLIDERCRANK",
     "mjTRN_TENDON",
     "mjTRN_SITE",
     "mjTRN_UNDEFINED"]
)(0, 1, 2, 3, 4, 1000)

mjtDyn = collections.namedtuple(
    "mjtDyn",
    ["mjDYN_NONE",
     "mjDYN_INTEGRATOR",
     "mjDYN_FILTER",
     "mjDYN_USER"]
)(0, 1, 2, 3)

mjtGain = collections.namedtuple(
    "mjtGain",
    ["mjGAIN_FIXED",
     "mjGAIN_USER"]
)(0, 1)

mjtBias = collections.namedtuple(
    "mjtBias",
    ["mjBIAS_NONE",
     "mjBIAS_AFFINE",
     "mjBIAS_USER"]
)(0, 1, 2)

mjtObj = collections.namedtuple(
    "mjtObj",
    ["mjOBJ_UNKNOWN",
     "mjOBJ_BODY",
     "mjOBJ_XBODY",
     "mjOBJ_JOINT",
     "mjOBJ_DOF",
     "mjOBJ_GEOM",
     "mjOBJ_SITE",
     "mjOBJ_CAMERA",
     "mjOBJ_LIGHT",
     "mjOBJ_MESH",
     "mjOBJ_HFIELD",
     "mjOBJ_TEXTURE",
     "mjOBJ_MATERIAL",
     "mjOBJ_PAIR",
     "mjOBJ_EXCLUDE",
     "mjOBJ_EQUALITY",
     "mjOBJ_TENDON",
     "mjOBJ_ACTUATOR",
     "mjOBJ_SENSOR",
     "mjOBJ_NUMERIC",
     "mjOBJ_TEXT",
     "mjOBJ_TUPLE",
     "mjOBJ_KEY"]
)(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22)

mjtConstraint = collections.namedtuple(
    "mjtConstraint",
    ["mjCNSTR_EQUALITY",
     "mjCNSTR_FRICTION_DOF",
     "mjCNSTR_FRICTION_TENDON",
     "mjCNSTR_LIMIT_JOINT",
     "mjCNSTR_LIMIT_TENDON",
     "mjCNSTR_CONTACT_FRICTIONLESS",
     "mjCNSTR_CONTACT_PYRAMIDAL",
     "mjCNSTR_CONTACT_ELLIPTIC"]
)(0, 1, 2, 3, 4, 5, 6, 7)

mjtConstraintState = collections.namedtuple(
    "mjtConstraintState",
    ["mjCNSTRSTATE_SATISFIED",
     "mjCNSTRSTATE_QUADRATIC",
     "mjCNSTRSTATE_LINEARNEG",
     "mjCNSTRSTATE_LINEARPOS",
     "mjCNSTRSTATE_CONE"]
)(0, 1, 2, 3, 4)

mjtSensor = collections.namedtuple(
    "mjtSensor",
    ["mjSENS_TOUCH",
     "mjSENS_ACCELEROMETER",
     "mjSENS_VELOCIMETER",
     "mjSENS_GYRO",
     "mjSENS_FORCE",
     "mjSENS_TORQUE",
     "mjSENS_MAGNETOMETER",
     "mjSENS_RANGEFINDER",
     "mjSENS_JOINTPOS",
     "mjSENS_JOINTVEL",
     "mjSENS_TENDONPOS",
     "mjSENS_TENDONVEL",
     "mjSENS_ACTUATORPOS",
     "mjSENS_ACTUATORVEL",
     "mjSENS_ACTUATORFRC",
     "mjSENS_BALLQUAT",
     "mjSENS_BALLANGVEL",
     "mjSENS_FRAMEPOS",
     "mjSENS_FRAMEQUAT",
     "mjSENS_FRAMEXAXIS",
     "mjSENS_FRAMEYAXIS",
     "mjSENS_FRAMEZAXIS",
     "mjSENS_FRAMELINVEL",
     "mjSENS_FRAMEANGVEL",
     "mjSENS_FRAMELINACC",
     "mjSENS_FRAMEANGACC",
     "mjSENS_SUBTREECOM",
     "mjSENS_SUBTREELINVEL",
     "mjSENS_SUBTREEANGMOM",
     "mjSENS_USER"]
)(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29)

mjtStage = collections.namedtuple(
    "mjtStage",
    ["mjSTAGE_NONE",
     "mjSTAGE_POS",
     "mjSTAGE_VEL",
     "mjSTAGE_ACC"]
)(0, 1, 2, 3)

mjtDataType = collections.namedtuple(
    "mjtDataType",
    ["mjDATATYPE_REAL",
     "mjDATATYPE_POSITIVE",
     "mjDATATYPE_AXIS",
     "mjDATATYPE_QUATERNION"]
)(0, 1, 2, 3)

mjtGridPos = collections.namedtuple(
    "mjtGridPos",
    ["mjGRID_TOPLEFT",
     "mjGRID_TOPRIGHT",
     "mjGRID_BOTTOMLEFT",
     "mjGRID_BOTTOMRIGHT"]
)(0, 1, 2, 3)

mjtFramebuffer = collections.namedtuple(
    "mjtFramebuffer",
    ["mjFB_WINDOW",
     "mjFB_OFFSCREEN"]
)(0, 1)

mjtFontScale = collections.namedtuple(
    "mjtFontScale",
    ["mjFONTSCALE_100",
     "mjFONTSCALE_150",
     "mjFONTSCALE_200"]
)(100, 150, 200)

mjtFont = collections.namedtuple(
    "mjtFont",
    ["mjFONT_NORMAL",
     "mjFONT_SHADOW",
     "mjFONT_BIG"]
)(0, 1, 2)

mjtCatBit = collections.namedtuple(
    "mjtCatBit",
    ["mjCAT_STATIC",
     "mjCAT_DYNAMIC",
     "mjCAT_DECOR",
     "mjCAT_ALL"]
)(1, 2, 4, 7)

mjtMouse = collections.namedtuple(
    "mjtMouse",
    ["mjMOUSE_NONE",
     "mjMOUSE_ROTATE_V",
     "mjMOUSE_ROTATE_H",
     "mjMOUSE_MOVE_V",
     "mjMOUSE_MOVE_H",
     "mjMOUSE_ZOOM",
     "mjMOUSE_SELECT"]
)(0, 1, 2, 3, 4, 5, 6)

mjtPertBit = collections.namedtuple(
    "mjtPertBit",
    ["mjPERT_TRANSLATE",
     "mjPERT_ROTATE"]
)(1, 2)

mjtCamera = collections.namedtuple(
    "mjtCamera",
    ["mjCAMERA_FREE",
     "mjCAMERA_TRACKING",
     "mjCAMERA_FIXED",
     "mjCAMERA_USER"]
)(0, 1, 2, 3)

mjtLabel = collections.namedtuple(
    "mjtLabel",
    ["mjLABEL_NONE",
     "mjLABEL_BODY",
     "mjLABEL_JOINT",
     "mjLABEL_GEOM",
     "mjLABEL_SITE",
     "mjLABEL_CAMERA",
     "mjLABEL_LIGHT",
     "mjLABEL_TENDON",
     "mjLABEL_ACTUATOR",
     "mjLABEL_CONSTRAINT",
     "mjLABEL_SELECTION",
     "mjLABEL_SELPNT",
     "mjLABEL_CONTACTFORCE",
     "mjNLABEL"]
)(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

mjtFrame = collections.namedtuple(
    "mjtFrame",
    ["mjFRAME_NONE",
     "mjFRAME_BODY",
     "mjFRAME_GEOM",
     "mjFRAME_SITE",
     "mjFRAME_CAMERA",
     "mjFRAME_LIGHT",
     "mjFRAME_WORLD",
     "mjNFRAME"]
)(0, 1, 2, 3, 4, 5, 6, 7)

mjtVisFlag = collections.namedtuple(
    "mjtVisFlag",
    ["mjVIS_CONVEXHULL",
     "mjVIS_TEXTURE",
     "mjVIS_JOINT",
     "mjVIS_ACTUATOR",
     "mjVIS_CAMERA",
     "mjVIS_LIGHT",
     "mjVIS_CONSTRAINT",
     "mjVIS_INERTIA",
     "mjVIS_PERTFORCE",
     "mjVIS_PERTOBJ",
     "mjVIS_CONTACTPOINT",
     "mjVIS_CONTACTFORCE",
     "mjVIS_CONTACTSPLIT",
     "mjVIS_TRANSPARENT",
     "mjVIS_AUTOCONNECT",
     "mjVIS_COM",
     "mjVIS_SELECT",
     "mjVIS_STATIC",
     "mjNVISFLAG"]
)(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)

mjtRndFlag = collections.namedtuple(
    "mjtRndFlag",
    ["mjRND_SHADOW",
     "mjRND_WIREFRAME",
     "mjRND_REFLECTION",
     "mjRND_FOG",
     "mjRND_SKYBOX",
     "mjNRNDFLAG"]
)(0, 1, 2, 3, 4, 5)

mjtStereo = collections.namedtuple(
    "mjtStereo",
    ["mjSTEREO_NONE",
     "mjSTEREO_QUADBUFFERED",
     "mjSTEREO_SIDEBYSIDE"]
)(0, 1, 2)

# ----------------------------End of generated code----------------------------
