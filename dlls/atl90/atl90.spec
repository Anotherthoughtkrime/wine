10 stdcall AtlAdvise(ptr ptr ptr ptr)
11 stdcall AtlUnadvise(ptr ptr long)
12 stdcall AtlFreeMarshalStream(ptr)
13 stdcall AtlMarshalPtrInProc(ptr ptr ptr)
14 stdcall AtlUnmarshalPtr(ptr ptr ptr)
15 stdcall AtlComModuleGetClassObject(ptr ptr ptr ptr)
17 stdcall AtlComModuleRegisterClassObjects(ptr long long)
20 stdcall AtlComModuleRevokeClassObjects(ptr)
22 stdcall AtlComModuleUnregisterServer(ptr long ptr)
23 stdcall AtlUpdateRegistryFromResourceD(long wstr long ptr ptr) atl100.AtlUpdateRegistryFromResourceD
24 stdcall AtlWaitWithMessageLoop(long)
25 stub AtlSetErrorInfo
26 stdcall AtlCreateTargetDC(long ptr)
27 stdcall AtlHiMetricToPixel(ptr ptr)
28 stdcall AtlPixelToHiMetric(ptr ptr)
29 stub AtlDevModeW2A
30 stdcall AtlComPtrAssign(ptr ptr)
31 stdcall AtlComQIPtrAssign(ptr ptr ptr)
32 stdcall AtlInternalQueryInterface(ptr ptr ptr ptr)
34 stdcall AtlGetVersion(ptr)
35 stdcall AtlAxDialogBoxW(long wstr long ptr long)
36 stdcall AtlAxDialogBoxA(long str long ptr long)
37 stdcall AtlAxCreateDialogW(long wstr long ptr long)
38 stdcall AtlAxCreateDialogA(long str long ptr long)
39 stdcall AtlAxCreateControl(ptr ptr ptr ptr)
40 stdcall AtlAxCreateControlEx(ptr ptr ptr ptr ptr ptr ptr)
41 stdcall AtlAxAttachControl(ptr ptr ptr)
42 stdcall AtlAxWinInit()
43 stdcall AtlWinModuleAddCreateWndData(ptr ptr ptr)
44 stdcall AtlWinModuleExtractCreateWndData(ptr)
45 stub AtlWinModuleRegisterWndClassInfoW
46 stub AtlWinModuleRegisterWndClassInfoA
47 stdcall AtlAxGetControl(long ptr)
48 stdcall AtlAxGetHost(long ptr)
49 stdcall AtlRegisterClassCategoriesHelper(ptr ptr long)
50 stdcall AtlIPersistStreamInit_Load(ptr ptr ptr ptr)
51 stdcall AtlIPersistStreamInit_Save(ptr long ptr ptr ptr)
52 stdcall AtlIPersistPropertyBag_Load(ptr ptr ptr ptr ptr)
53 stub AtlIPersistPropertyBag_Save
54 stdcall AtlGetObjectSourceInterface(ptr ptr ptr ptr ptr)
56 stdcall AtlLoadTypeLib(long wstr ptr ptr)
58 stdcall AtlModuleAddTermFunc(ptr ptr long)
59 stub AtlAxCreateControlLic
60 stub AtlAxCreateControlLicEx
61 stdcall AtlCreateRegistrar(ptr) atl100.AtlCreateRegistrar
62 stub AtlWinModuleRegisterClassExW
63 stub AtlWinModuleRegisterClassExA
64 stdcall AtlCallTermFunc(ptr)
65 stdcall AtlWinModuleInit(ptr)
66 stub AtlWinModuleTerm
67 stdcall AtlSetPerUserRegistration(long)
68 stdcall AtlGetPerUserRegistration(ptr)
