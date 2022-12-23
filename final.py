# state file generated using paraview version 5.11.0-RC2
import sys, os
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 11

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()
directories = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
for num in directories:
 for file in os.listdir(f"/Users/macbook/OneDrive - UvA/mantle{num}"):
  

# Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1784, 1128]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.OrientationAxesVisibility = 0
    renderView1.CenterOfRotation = [-3093.128963605495, -12.621379412658825, -51.8330078125]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [32538.07420773949, -12.621379412658825, -448.7952673895133]
    renderView1.CameraFocalPoint = [-4180.908036804926, -12.621379412658825, -39.71421303755679]
    renderView1.CameraViewUp = [0.01114016904586556, 0.0, 0.9999379463914897]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 9504.161689198081
    renderView1.UseColorPaletteForBackground = 0
    renderView1.Background = [0.9835507743953612, 0.9876707103074693, 1.0]
    renderView1.BackEnd = 'OSPRay raycaster'
    renderView1.OSPRayMaterialLibrary = materialLibrary1
    
    # init the 'GridAxes3DActor' selected for 'AxesGrid'
    renderView1.AxesGrid.Visibility = 1
    renderView1.AxesGrid.XTitle = 'X [km]'
    renderView1.AxesGrid.YTitle = 'Y [km]'
    renderView1.AxesGrid.ZTitle = 'Z [km]'
    renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.0]
    renderView1.AxesGrid.XAxisUseCustomLabels = 1
    renderView1.AxesGrid.YAxisUseCustomLabels = 1
    renderView1.AxesGrid.YAxisLabels = [0.0, -3000.0, 0.0, 3000.0, 0.0]
    renderView1.AxesGrid.ZAxisUseCustomLabels = 1
    renderView1.AxesGrid.ZAxisLabels = [3000.0, 0.0, -3000.0]
    
    SetActiveView(None)
    
    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------
    
    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView1)
    layout1.SetSize(1784, 1128)
    
    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView1)
    
    # Create a new 'Render View'
    spherical001nc = NetCDFReader(registrationName=f'{file}', FileName=[f'/Users/macbook/OneDrive - UvA/mantle{num}/{file}'])
    spherical001nc.Dimensions = '(lat, r, lon)'

#    spherical001nc.Dimensions = '(lat, r, lon)'
    
    # create a new 'Calculator'
    calculator1 = Calculator(registrationName='Calculator1', Input=spherical001nc)
    calculator1.AttributeType = 'Cell Data'
    calculator1.ResultArrayName = 'V'
    calculator1.Function = 'iHat*vx+jHat*vy+kHat*vz'
    
    # create a new 'Threshold'
    threshold1 = Threshold(registrationName='Threshold1', Input=calculator1)
    threshold1.Scalars = ['CELLS', 'temperature anomaly']
    threshold1.LowerThreshold = -300.57
    threshold1.UpperThreshold = 130.17787170410156
    threshold1.ThresholdMethod = 'Below Lower Threshold'
    
    # create a new 'Text'
    text1 = Text(registrationName='Text1')
    text1.Text = """
    
    
    
    
    
    
    Active Up      
    
    
    Passive Up     
    
    
    Stagnant        
    
    
    Passive Down
    
    
    Active Down """
    
    # create a new 'Calculator'
    calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
    calculator2.ResultArrayName = 'V Orientation'
    calculator2.Function = 'coordsX*iHat+coordsY*jHat+coordsZ*kHat'
    calculator2.ReplaceInvalidResults = 0
    
    # create a new 'Point Data to Cell Data'
    pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=calculator2)
    pointDatatoCellData1.PointDataArraytoprocess = ['V Orientation']
    
    # create a new 'Glyph'
    glyph2 = Glyph(registrationName='Glyph2', Input=calculator2,
        GlyphType='Arrow')
    glyph2.OrientationArray = ['POINTS', 'V Orientation']
    glyph2.ScaleArray = ['POINTS', 'No scale array']
    glyph2.ScaleFactor = 841.9163207754932
    glyph2.GlyphTransform = 'Transform2'
    glyph2.MaximumNumberOfSamplePoints = 1000
    
    # create a new 'Clip'
    clip3 = Clip(registrationName='Clip3', Input=threshold1)
    clip3.ClipType = 'Plane'
    clip3.HyperTreeGridClipper = 'Plane'
    clip3.Scalars = ['CELLS', 'spin transition-induced density anomaly']
    clip3.Value = 33.638343811035156
    
    # init the 'Plane' selected for 'ClipType'
    clip3.ClipType.Origin = [-78.18892609919112, 90.95640488990375, -51.661018685258114]
    
    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip3.HyperTreeGridClipper.Origin = [-78.18892609919112, 90.95640488990375, -51.661018685258114]
    
    # create a new 'Glyph'
    glyph1 = Glyph(registrationName='Glyph1', Input=calculator1,
        GlyphType='Arrow')
    glyph1.OrientationArray = ['CELLS', 'V']
    glyph1.ScaleArray = ['POINTS', 'No scale array']
    glyph1.VectorScaleMode = 'Scale by Components'
    glyph1.ScaleFactor = 574.0338550741999
    glyph1.GlyphTransform = 'Transform2'
    glyph1.MaximumNumberOfSamplePoints = 1000
    
    # create a new 'Threshold'
    threshold2 = Threshold(registrationName='Threshold2', Input=calculator2)
    threshold2.Scalars = ['CELLS', 'temperature anomaly']
    threshold2.LowerThreshold = -166.5840301513672
    threshold2.UpperThreshold = 300.0
    threshold2.ThresholdMethod = 'Above Upper Threshold'
    
    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=threshold2)
    clip1.ClipType = 'Plane'
    clip1.HyperTreeGridClipper = 'Plane'
    clip1.Scalars = ['CELLS', 'spin transition-induced density anomaly']
    clip1.Value = -47.8149528503418
    
    # init the 'Plane' selected for 'ClipType'
    clip1.ClipType.Origin = [170.6366040390103, -6.211839175327896, 314.23650568121457]
    
    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip1.HyperTreeGridClipper.Origin = [170.6366040390103, -6.211839175327896, 314.23650568121457]
    
    # create a new 'Calculator'
    calculator3 = Calculator(registrationName='Calculator3', Input=pointDatatoCellData1)
    calculator3.AttributeType = 'Cell Data'
    calculator3.ResultArrayName = 'Angle'
    calculator3.Function = '"V Orientation_X"*V_X+"V Orientation_Y"*V_Y+"V Orientation_Z"*V_Z'
    
    # create a new 'Calculator'
    calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
    calculator4.AttributeType = 'Cell Data'
    calculator4.ResultArrayName = 'Magn'
    calculator4.Function = 'sqrt(vx^2+vy^2+vz^2)*1000000000'
    calculator4.ResultArrayType = 'Float'
    
    # create a new 'Glyph'
    glyph4 = Glyph(registrationName='Glyph4', Input=calculator4,
        GlyphType='Arrow')
    glyph4.OrientationArray = ['CELLS', 'V']
    glyph4.ScaleArray = ['CELLS', 'Magn']
    glyph4.ScaleFactor = 350.0
    glyph4.GlyphTransform = 'Transform2'
    glyph4.MaximumNumberOfSamplePoints = 7500
    
    # init the 'Arrow' selected for 'GlyphType'
    glyph4.GlyphType.TipLength = 0.41
    
    # create a new 'Clip'
    clip2 = Clip(registrationName='Clip2', Input=glyph4)
    clip2.ClipType = 'Plane'
    clip2.HyperTreeGridClipper = 'Plane'
    clip2.Scalars = ['POINTS', 'Magn']
    clip2.Value = 0.024667045296155266
    
    # init the 'Plane' selected for 'ClipType'
    clip2.ClipType.Origin = [34.662353515625, -41.550537109375, -13.271484375]
    clip2.ClipType.Normal = [0.9999285420744812, -0.003437377231270346, -0.011449680457218208]
    
    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip2.HyperTreeGridClipper.Origin = [34.662353515625, -41.550537109375, -13.271484375]
    
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from text1
    text1Display = Show(text1, renderView1, 'TextSourceRepresentation')
    
    # trace defaults for the display properties.
    text1Display.WindowLocation = 'Upper Right Corner'
    text1Display.Color = [0.0, 0.0, 0.0]
    
    # show data from clip1
    clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')
    
    # get 2D transfer function for 'temperatureanomaly'
    temperatureanomalyTF2D = GetTransferFunction2D('temperatureanomaly')
    temperatureanomalyTF2D.ScalarRangeInitialized = 1
    temperatureanomalyTF2D.Range = [-1099.197509765625, -151.3402214050293, -1099.197509765625, -151.3402214050293]
    
    # get color transfer function/color map for 'temperatureanomaly'
    temperatureanomalyLUT = GetColorTransferFunction('temperatureanomaly')
    temperatureanomalyLUT.EnableOpacityMapping = 1
    temperatureanomalyLUT.TransferFunction2D = temperatureanomalyTF2D
    temperatureanomalyLUT.RGBPoints = [-1099.197509765625, 0.0, 0.0, 0.34902, -1030.3021697998047, 0.039216, 0.062745, 0.380392, -961.4068298339844, 0.062745, 0.117647, 0.411765, -892.5114898681641, 0.090196, 0.184314, 0.45098, -823.6161499023438, 0.12549, 0.262745, 0.501961, -754.7208099365234, 0.160784, 0.337255, 0.541176, -685.8254699707031, 0.2, 0.396078, 0.568627, -616.9301300048828, 0.239216, 0.454902, 0.6, -548.0347900390625, 0.286275, 0.521569, 0.65098, -479.1394500732422, 0.337255, 0.592157, 0.701961, -410.2441101074219, 0.388235, 0.654902, 0.74902, -341.34877014160156, 0.466667, 0.737255, 0.819608, -272.45343017578125, 0.572549, 0.819608, 0.878431, -203.55809020996094, 0.654902, 0.866667, 0.909804, -134.66275024414062, 0.752941, 0.917647, 0.941176, -65.76741027832031, 0.823529, 0.956863, 0.968627, 3.1279296875, 0.988235, 0.960784, 0.901961, 3.1279296875, 0.941176, 0.984314, 0.988235, 47.220947265625, 0.988235, 0.945098, 0.85098, 91.31396484375, 0.980392, 0.898039, 0.784314, 140.91860961914062, 0.968627, 0.835294, 0.698039, 209.81394958496094, 0.94902, 0.733333, 0.588235, 278.70928955078125, 0.929412, 0.65098, 0.509804, 347.60462951660156, 0.909804, 0.564706, 0.435294, 416.4999694824219, 0.878431, 0.458824, 0.352941, 485.3953094482422, 0.839216, 0.388235, 0.286275, 554.2906494140625, 0.760784, 0.294118, 0.211765, 623.1859893798828, 0.701961, 0.211765, 0.168627, 692.0813293457031, 0.65098, 0.156863, 0.129412, 760.9766693115234, 0.6, 0.094118, 0.094118, 829.8720092773438, 0.54902, 0.066667, 0.098039, 898.7673492431641, 0.501961, 0.05098, 0.12549, 967.6626892089844, 0.45098, 0.054902, 0.172549, 1036.5580291748047, 0.4, 0.054902, 0.192157, 1105.453369140625, 0.34902, 0.070588, 0.211765]
    temperatureanomalyLUT.ColorSpace = 'Lab'
    temperatureanomalyLUT.NanColor = [0.25, 0.0, 0.0]
    temperatureanomalyLUT.ScalarRangeInitialized = 1.0
    
    # get opacity transfer function/opacity map for 'temperatureanomaly'
    temperatureanomalyPWF = GetOpacityTransferFunction('temperatureanomaly')
    temperatureanomalyPWF.Points = [-1099.197509765625, 1.0, 0.5, 0.0, -151.69305419921875, 0.957207202911377, 0.5, 0.0, 151.75608825683594, 0.7545045018196106, 0.5, 0.0, 777.23291015625, 0.619369387626648, 0.5, 0.0, 1105.453369140625, 0.0, 0.5, 0.0]
    temperatureanomalyPWF.ScalarRangeInitialized = 1
    
    # trace defaults for the display properties.
    clip1Display.Representation = 'Surface'
    clip1Display.ColorArrayName = ['CELLS', 'temperature anomaly']
    clip1Display.LookupTable = temperatureanomalyLUT
    clip1Display.SelectTCoordArray = 'None'
    clip1Display.SelectNormalArray = 'None'
    clip1Display.SelectTangentArray = 'None'
    clip1Display.OSPRayScaleArray = 'V Orientation'
    clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    clip1Display.SelectOrientationVectors = 'V Orientation'
    clip1Display.ScaleFactor = 1267.9625712084232
    clip1Display.SelectScaleArray = 'None'
    clip1Display.GlyphType = 'Arrow'
    clip1Display.GlyphTableIndexArray = 'None'
    clip1Display.GaussianRadius = 63.398128560421156
    clip1Display.SetScaleArray = ['POINTS', 'V Orientation']
    clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
    clip1Display.OpacityArray = ['POINTS', 'V Orientation']
    clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
    clip1Display.DataAxesGrid = 'GridAxesRepresentation'
    clip1Display.PolarAxes = 'PolarAxesRepresentation'
    clip1Display.ScalarOpacityFunction = temperatureanomalyPWF
    clip1Display.ScalarOpacityUnitDistance = 518.9276444888905
    clip1Display.OpacityArrayName = ['POINTS', 'V Orientation']
    clip1Display.SelectInputVectors = ['POINTS', 'V Orientation']
    clip1Display.WriteLog = ''
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    clip1Display.ScaleTransferFunction.Points = [-6013.992923462821, 0.0, 0.5, 0.0, 170.6366040390103, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    clip1Display.OpacityTransferFunction.Points = [-6013.992923462821, 0.0, 0.5, 0.0, 170.6366040390103, 1.0, 0.5, 0.0]
    
    # show data from clip3
    clip3Display = Show(clip3, renderView1, 'UnstructuredGridRepresentation')
    
    # trace defaults for the display properties.
    clip3Display.Representation = 'Surface'
    clip3Display.ColorArrayName = ['CELLS', 'temperature anomaly']
    clip3Display.LookupTable = temperatureanomalyLUT
    clip3Display.Specular = 0.63
    clip3Display.SelectTCoordArray = 'None'
    clip3Display.SelectNormalArray = 'None'
    clip3Display.SelectTangentArray = 'None'
    clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
    clip3Display.SelectOrientationVectors = 'V'
    clip3Display.ScaleFactor = 1244.7670686202591
    clip3Display.SelectScaleArray = 'None'
    clip3Display.GlyphType = 'Arrow'
    clip3Display.GlyphTableIndexArray = 'None'
    clip3Display.GaussianRadius = 62.238353431012946
    clip3Display.SetScaleArray = [None, '']
    clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
    clip3Display.OpacityArray = [None, '']
    clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
    clip3Display.DataAxesGrid = 'GridAxesRepresentation'
    clip3Display.PolarAxes = 'PolarAxesRepresentation'
    clip3Display.ScalarOpacityFunction = temperatureanomalyPWF
    clip3Display.ScalarOpacityUnitDistance = 535.4149071943298
    clip3Display.OpacityArrayName = ['CELLS', 'V']
    clip3Display.SelectInputVectors = [None, '']
    clip3Display.WriteLog = ''
    
    # show data from clip2
    clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')
    
    # get 2D transfer function for 'Angle'
    angleTF2D = GetTransferFunction2D('Angle')
    
    # get color transfer function/color map for 'Angle'
    angleLUT = GetColorTransferFunction('Angle')
    angleLUT.TransferFunction2D = angleTF2D
    angleLUT.RGBPoints = [-5.3005095466254935e-05, 0.267004, 0.004874, 0.329415, -5.272384303563637e-05, 0.26851, 0.009605, 0.335427, -5.2442662316499344e-05, 0.269944, 0.014625, 0.341379, -5.2161409885880775e-05, 0.271305, 0.019942, 0.347269, -5.188022916674376e-05, 0.272594, 0.025563, 0.353093, -5.159897673612519e-05, 0.273809, 0.031497, 0.358853, -5.131779601698816e-05, 0.274952, 0.037752, 0.364543, -5.10365435863696e-05, 0.276022, 0.044167, 0.370164, -5.0755291155751036e-05, 0.277018, 0.050344, 0.375715, -5.047411043661401e-05, 0.277941, 0.056324, 0.381191, -5.019285800599544e-05, 0.278791, 0.062145, 0.386592, -4.991167728685842e-05, 0.279566, 0.067836, 0.391917, -4.9630424856239854e-05, 0.280267, 0.073417, 0.397163, -4.9349244137102825e-05, 0.280894, 0.078907, 0.402329, -4.906799170648426e-05, 0.281446, 0.08432, 0.407414, -4.87867392758657e-05, 0.281924, 0.089666, 0.412415, -4.850555855672867e-05, 0.282327, 0.094955, 0.417331, -4.82243061261101e-05, 0.282656, 0.100196, 0.42216, -4.794312540697309e-05, 0.28291, 0.105393, 0.426902, -4.766187297635451e-05, 0.283091, 0.110553, 0.431554, -4.738069225721749e-05, 0.283197, 0.11568, 0.436115, -4.7099439826598926e-05, 0.283229, 0.120777, 0.440584, -4.681818739598036e-05, 0.283187, 0.125848, 0.44496, -4.6537006676843335e-05, 0.283072, 0.130895, 0.449241, -4.625575424622477e-05, 0.282884, 0.13592, 0.453427, -4.597457352708775e-05, 0.282623, 0.140926, 0.457517, -4.569332109646918e-05, 0.28229, 0.145912, 0.46151, -4.541214037733216e-05, 0.281887, 0.150881, 0.465405, -4.513088794671359e-05, 0.281412, 0.155834, 0.469201, -4.484970722757657e-05, 0.280868, 0.160771, 0.472899, -4.4568454796958e-05, 0.280255, 0.165693, 0.476498, -4.428720236633943e-05, 0.279574, 0.170599, 0.479997, -4.400602164720241e-05, 0.278826, 0.17549, 0.483397, -4.372476921658384e-05, 0.278012, 0.180367, 0.486697, -4.3443588497446816e-05, 0.277134, 0.185228, 0.489898, -4.3162336066828254e-05, 0.276194, 0.190074, 0.493001, -4.288115534769123e-05, 0.275191, 0.194905, 0.496005, -4.259990291707266e-05, 0.274128, 0.199721, 0.498911, -4.23186504864541e-05, 0.273006, 0.20452, 0.501721, -4.203746976731708e-05, 0.271828, 0.209303, 0.504434, -4.175621733669851e-05, 0.270595, 0.214069, 0.507052, -4.1475036617561487e-05, 0.269308, 0.218818, 0.509577, -4.119378418694292e-05, 0.267968, 0.223549, 0.512008, -4.0912603467805895e-05, 0.26658, 0.228262, 0.514349, -4.0631351037187326e-05, 0.265145, 0.232956, 0.516599, -4.035009860656876e-05, 0.263663, 0.237631, 0.518762, -4.006891788743174e-05, 0.262138, 0.242286, 0.520837, -3.9787665456813165e-05, 0.260571, 0.246922, 0.522828, -3.9506484737676144e-05, 0.258965, 0.251537, 0.524736, -3.922523230705758e-05, 0.257322, 0.25613, 0.526563, -3.894405158792056e-05, 0.255645, 0.260703, 0.528312, -3.866279915730199e-05, 0.253935, 0.265254, 0.529983, -3.838154672668343e-05, 0.252194, 0.269783, 0.531579, -3.8100366007546405e-05, 0.250425, 0.27429, 0.533103, -3.781911357692783e-05, 0.248629, 0.278775, 0.534556, -3.7537932857790814e-05, 0.246811, 0.283237, 0.535941, -3.7256680427172245e-05, 0.244972, 0.287675, 0.53726, -3.697549970803522e-05, 0.243113, 0.292092, 0.538516, -3.669424727741665e-05, 0.241237, 0.296485, 0.539709, -3.6412994846798084e-05, 0.239346, 0.300855, 0.540844, -3.613181412766106e-05, 0.237441, 0.305202, 0.541921, -3.585056169704249e-05, 0.235526, 0.309527, 0.542944, -3.556938097790547e-05, 0.233603, 0.313828, 0.543914, -3.52881285472869e-05, 0.231674, 0.318106, 0.544834, -3.5006947828149886e-05, 0.229739, 0.322361, 0.545706, -3.472569539753132e-05, 0.227802, 0.326594, 0.546532, -3.4444442966912755e-05, 0.225863, 0.330805, 0.547314, -3.416326224777573e-05, 0.223925, 0.334994, 0.548053, -3.388200981715716e-05, 0.221989, 0.339161, 0.548752, -3.360082909802014e-05, 0.220057, 0.343307, 0.549413, -3.331957666740157e-05, 0.21813, 0.347432, 0.550038, -3.303839594826455e-05, 0.21621, 0.351535, 0.550627, -3.275714351764598e-05, 0.214298, 0.355619, 0.551184, -3.247589108702741e-05, 0.212395, 0.359683, 0.55171, -3.219471036789039e-05, 0.210503, 0.363727, 0.552206, -3.191345793727183e-05, 0.208623, 0.367752, 0.552675, -3.16322772181348e-05, 0.206756, 0.371758, 0.553117, -3.1351024787516236e-05, 0.204903, 0.375746, 0.553533, -3.1069844068379214e-05, 0.203063, 0.379716, 0.553925, -3.0788591637760644e-05, 0.201239, 0.38367, 0.554294, -3.0507410918623626e-05, 0.19943, 0.387607, 0.554642, -3.0226158488005057e-05, 0.197636, 0.391528, 0.554969, -2.994490605738649e-05, 0.19586, 0.395433, 0.555276, -2.9663725338249465e-05, 0.1941, 0.399323, 0.555565, -2.93824729076309e-05, 0.192357, 0.403199, 0.555836, -2.9101292188493877e-05, 0.190631, 0.407061, 0.556089, -2.8820039757875308e-05, 0.188923, 0.41091, 0.556326, -2.853885903873829e-05, 0.187231, 0.414746, 0.556547, -2.8257606608119717e-05, 0.185556, 0.41857, 0.556753, -2.797635417750115e-05, 0.183898, 0.422383, 0.556944, -2.769517345836413e-05, 0.182256, 0.426184, 0.55712, -2.7413921027745563e-05, 0.180629, 0.429975, 0.557282, -2.713274030860854e-05, 0.179019, 0.433756, 0.55743, -2.6851487877989975e-05, 0.177423, 0.437527, 0.557565, -2.6570307158852953e-05, 0.175841, 0.44129, 0.557685, -2.628905472823438e-05, 0.174274, 0.445044, 0.557792, -2.6007802297615815e-05, 0.172719, 0.448791, 0.557885, -2.5726621578478793e-05, 0.171176, 0.45253, 0.557965, -2.5445369147860227e-05, 0.169646, 0.456262, 0.55803, -2.51641884287232e-05, 0.168126, 0.459988, 0.558082, -2.488293599810464e-05, 0.166617, 0.463708, 0.558119, -2.4601755278967613e-05, 0.165117, 0.467423, 0.558141, -2.4320502848349044e-05, 0.163625, 0.471133, 0.558148, -2.4039250417730478e-05, 0.162142, 0.474838, 0.55814, -2.3758069698593456e-05, 0.160665, 0.47854, 0.558115, -2.3476817267974894e-05, 0.159194, 0.482237, 0.558073, -2.319563654883787e-05, 0.157729, 0.485932, 0.558013, -2.2914384118219302e-05, 0.15627, 0.489624, 0.557936, -2.2633203399082277e-05, 0.154815, 0.493313, 0.55784, -2.2351950968463708e-05, 0.153364, 0.497, 0.557724, -2.2070698537845145e-05, 0.151918, 0.500685, 0.557587, -2.1789517818708123e-05, 0.150476, 0.504369, 0.55743, -2.150826538808956e-05, 0.149039, 0.508051, 0.55725, -2.1227084668952532e-05, 0.147607, 0.511733, 0.557049, -2.0945832238333963e-05, 0.14618, 0.515413, 0.556823, -2.066465151919694e-05, 0.144759, 0.519093, 0.556572, -2.0383399088578378e-05, 0.143343, 0.522773, 0.556295, -2.010214665795981e-05, 0.141935, 0.526453, 0.555991, -1.9820965938822787e-05, 0.140536, 0.530132, 0.555659, -1.953971350820421e-05, 0.139147, 0.533812, 0.555298, -1.9258532789067196e-05, 0.13777, 0.537492, 0.554906, -1.8977280358448626e-05, 0.136408, 0.541173, 0.554483, -1.8696099639311604e-05, 0.135066, 0.544853, 0.554029, -1.8414847208693042e-05, 0.133743, 0.548535, 0.553541, -1.8133594778074473e-05, 0.132444, 0.552216, 0.553018, -1.7852414058937444e-05, 0.131172, 0.555899, 0.552459, -1.7571161628318875e-05, 0.129933, 0.559582, 0.551864, -1.728998090918186e-05, 0.128729, 0.563265, 0.551229, -1.700872847856329e-05, 0.127568, 0.566949, 0.550556, -1.6727547759426268e-05, 0.126453, 0.570633, 0.549841, -1.64462953288077e-05, 0.125394, 0.574318, 0.549086, -1.6165114609670677e-05, 0.124395, 0.578002, 0.548287, -1.5883862179052114e-05, 0.123463, 0.581687, 0.547445, -1.5602609748433545e-05, 0.122606, 0.585371, 0.546557, -1.5321429029296523e-05, 0.121831, 0.589055, 0.545623, -1.5040176598677954e-05, 0.121148, 0.592739, 0.544641, -1.4758995879540939e-05, 0.120565, 0.596422, 0.543611, -1.4477743448922363e-05, 0.120092, 0.600104, 0.54253, -1.419656272978534e-05, 0.119738, 0.603785, 0.5414, -1.3915310299166778e-05, 0.119512, 0.607464, 0.540218, -1.3634057868548209e-05, 0.119423, 0.611141, 0.538982, -1.3352877149411187e-05, 0.119483, 0.614817, 0.537692, -1.3071624718792617e-05, 0.119699, 0.61849, 0.536347, -1.2790443999655602e-05, 0.120081, 0.622161, 0.534946, -1.2509191569037026e-05, 0.120638, 0.625828, 0.533488, -1.2228010849900004e-05, 0.12138, 0.629492, 0.531973, -1.1946758419281442e-05, 0.122312, 0.633153, 0.530398, -1.1665505988662872e-05, 0.123444, 0.636809, 0.528763, -1.138432526952585e-05, 0.12478, 0.640461, 0.527068, -1.1103072838907281e-05, 0.126326, 0.644107, 0.525311, -1.0821892119770266e-05, 0.128087, 0.647749, 0.523491, -1.054063968915169e-05, 0.130067, 0.651384, 0.521608, -1.0259458970014668e-05, 0.132268, 0.655014, 0.519661, -9.978206539396105e-06, 0.134692, 0.658636, 0.517649, -9.696954108777536e-06, 0.137339, 0.662252, 0.515571, -9.415773389640514e-06, 0.14021, 0.665859, 0.513427, -9.134520959021945e-06, 0.143303, 0.669459, 0.511215, -8.85334023988493e-06, 0.146616, 0.67305, 0.508936, -8.572087809266354e-06, 0.150148, 0.676631, 0.506589, -8.290907090129332e-06, 0.153894, 0.680203, 0.504172, -8.009654659510769e-06, 0.157851, 0.683765, 0.501686, -7.7284022288922e-06, 0.162016, 0.687316, 0.499129, -7.447221509755178e-06, 0.166383, 0.690856, 0.496502, -7.1659690791366085e-06, 0.170948, 0.694384, 0.493803, -6.8847883599995865e-06, 0.175707, 0.6979, 0.491033, -6.603535929381017e-06, 0.180653, 0.701402, 0.488189, -6.322355210243995e-06, 0.185783, 0.704891, 0.485273, -6.041102779625433e-06, 0.19109, 0.708366, 0.482284, -5.759850349006863e-06, 0.196571, 0.711827, 0.479221, -5.4786696298698414e-06, 0.202219, 0.715272, 0.476084, -5.197417199251272e-06, 0.20803, 0.718701, 0.472873, -4.91623648011425e-06, 0.214, 0.722114, 0.469588, -4.634984049495681e-06, 0.220124, 0.725509, 0.466226, -4.353803330358659e-06, 0.226397, 0.728888, 0.462789, -4.072550899740096e-06, 0.232815, 0.732247, 0.459277, -3.791298469121527e-06, 0.239374, 0.735588, 0.455688, -3.5101177499844983e-06, 0.24607, 0.73891, 0.452024, -3.228865319365936e-06, 0.252899, 0.742211, 0.448284, -2.947684600228914e-06, 0.259857, 0.745492, 0.444467, -2.6664321696103513e-06, 0.266941, 0.748751, 0.440573, -2.3852514504733226e-06, 0.274149, 0.751988, 0.436601, -2.10399901985476e-06, 0.281477, 0.755203, 0.432552, -1.8228183007177313e-06, 0.288921, 0.758394, 0.428426, -1.541565870099162e-06, 0.296479, 0.761561, 0.424223, -1.2603134394805995e-06, 0.304148, 0.764704, 0.419943, -9.791327203435775e-07, 0.311925, 0.767822, 0.415586, -6.97880289725015e-07, 0.319809, 0.770914, 0.411152, -4.1669957058798623e-07, 0.327796, 0.77398, 0.40664, -1.354471399694237e-07, 0.335885, 0.777018, 0.402049, 1.4573357916759826e-07, 0.344074, 0.780029, 0.397381, 4.2698600978617433e-07, 0.35236, 0.783011, 0.392636, 7.082384404047369e-07, 0.360741, 0.785964, 0.387814, 9.894191595417588e-07, 0.369214, 0.788888, 0.382914, 1.2706715901603213e-06, 0.377779, 0.791781, 0.377939, 1.55185230929735e-06, 0.386433, 0.794644, 0.372886, 1.8331047399159126e-06, 0.395174, 0.797475, 0.367757, 2.1142854590529346e-06, 0.404001, 0.800275, 0.362552, 2.3955378896715107e-06, 0.412913, 0.803041, 0.357269, 2.6767903202900664e-06, 0.421908, 0.805774, 0.35191, 2.957971039427095e-06, 0.430983, 0.808473, 0.346476, 3.2392234700456577e-06, 0.440137, 0.811138, 0.340967, 3.5204041891826864e-06, 0.449368, 0.813768, 0.335384, 3.5204041891826864e-06, 0.458674, 0.816363, 0.329727, 4.082837338938271e-06, 0.468053, 0.818921, 0.323998, 4.364089769556847e-06, 0.477504, 0.821444, 0.318195, 4.6453422001754095e-06, 0.487026, 0.823929, 0.312321, 4.6453422001754095e-06, 0.496615, 0.826376, 0.306377, 5.207775349930994e-06, 0.506271, 0.828786, 0.300362, 5.488956069068023e-06, 0.515992, 0.831158, 0.294279, 5.7702084996865785e-06, 0.525776, 0.833491, 0.288127, 6.051389218823607e-06, 0.535621, 0.835785, 0.281908, 6.3326416494421765e-06, 0.545524, 0.838039, 0.275626, 6.613894080060739e-06, 0.555484, 0.840254, 0.269281, 6.895074799197768e-06, 0.565498, 0.84243, 0.262877, 7.17632722981633e-06, 0.575563, 0.844566, 0.256415, 7.457507948953359e-06, 0.585678, 0.846661, 0.249897, 7.738760379571928e-06, 0.595839, 0.848717, 0.243329, 8.019941098708944e-06, 0.606045, 0.850733, 0.236712, 8.30119352932752e-06, 0.616293, 0.852709, 0.230052, 8.582445959946089e-06, 0.626579, 0.854645, 0.223353, 8.863626679083097e-06, 0.636902, 0.856542, 0.21662, 9.144879109701667e-06, 0.647257, 0.8584, 0.209861, 9.426059828838689e-06, 0.657642, 0.860219, 0.203082, 9.707312259457258e-06, 0.668054, 0.861999, 0.196293, 9.98849297859428e-06, 0.678489, 0.863742, 0.189503, 1.026974540921285e-05, 0.688944, 0.865448, 0.182725, 1.0550997839831432e-05, 0.699415, 0.867117, 0.175971, 1.083217855896844e-05, 0.709898, 0.868751, 0.169257, 1.111343098958701e-05, 0.720391, 0.87035, 0.162603, 1.1394611708724032e-05, 0.730889, 0.871916, 0.156029, 1.1675864139342601e-05, 0.741388, 0.873449, 0.149561, 1.1957044858479623e-05, 0.751884, 0.874951, 0.143228, 1.2238297289098179e-05, 0.762373, 0.876424, 0.137064, 1.25194780082352e-05, 0.772852, 0.877868, 0.131109, 1.280073043885377e-05, 0.783315, 0.879285, 0.125405, 1.308198286947234e-05, 0.79376, 0.880678, 0.120005, 1.3363163588609361e-05, 0.804182, 0.882046, 0.114965, 1.364441601922793e-05, 0.814576, 0.883393, 0.110347, 1.3925596738364953e-05, 0.82494, 0.88472, 0.106217, 1.4206849168983522e-05, 0.83527, 0.886029, 0.102646, 1.4488029888120544e-05, 0.845561, 0.887322, 0.099702, 1.4769282318739113e-05, 0.85581, 0.888601, 0.097452, 1.5050534749357682e-05, 0.866013, 0.889868, 0.095953, 1.5331715468494704e-05, 0.876168, 0.891125, 0.09525, 1.5612967899113274e-05, 0.886271, 0.892374, 0.095374, 1.5894148618250282e-05, 0.89632, 0.893616, 0.096335, 1.617540104886885e-05, 0.906311, 0.894855, 0.098125, 1.6456581768005873e-05, 0.916242, 0.896091, 0.100717, 1.6737834198624443e-05, 0.926106, 0.89733, 0.104071, 1.7019086629243026e-05, 0.935904, 0.89857, 0.108131, 1.7300267348380047e-05, 0.945636, 0.899815, 0.112838, 1.7581519778998617e-05, 0.9553, 0.901065, 0.118128, 1.7862700498135625e-05, 0.964894, 0.902323, 0.123941, 1.8143952928754195e-05, 0.974417, 0.90359, 0.130215, 1.8425133647891216e-05, 0.983868, 0.904867, 0.136897, 1.8706386078509786e-05, 0.993248, 0.906157, 0.143936]
    angleLUT.ColorSpace = 'Lab'
    angleLUT.NanColor = [1.0, 0.0, 0.0]
    angleLUT.NumberOfTableValues = 5
    angleLUT.ScalarRangeInitialized = 1.0
    angleLUT.Annotations = ['0', 'Stagnant', '0.000005890987048671968', 'Passive Up', '0.000014890987048671968', 'Active Up', '-0.000005890987048671968', 'Passive Down', '-0.000014890987048671968', 'Active Down']
    angleLUT.IndexedColors = [1.0, 1.0, 1.0, 0.047058823529411764, 0.5686274509803921, 0.13333333333333333, 0.0, 0.12549019607843137, 0.0, 0.00392156862745098, 0.48627450980392156, 0.788235294117647, 0.00392156862745098, 0.0784313725490196, 0.23529411764705882]
    angleLUT.IndexedOpacities = [1.0, 1.0, 1.0, 1.0, 1.0]
    
    # get opacity transfer function/opacity map for 'Angle'
    anglePWF = GetOpacityTransferFunction('Angle')
    anglePWF.Points = [-5.3005095466254935e-05, 0.0, 0.5, 0.0, 1.8706386078509786e-05, 1.0, 0.5, 0.0]
    anglePWF.ScalarRangeInitialized = 1
    
    # trace defaults for the display properties.
    clip2Display.Representation = 'Surface'
    clip2Display.ColorArrayName = ['POINTS', 'Angle']
    clip2Display.LookupTable = angleLUT
    clip2Display.Specular = 0.39
    clip2Display.SelectTCoordArray = 'None'
    clip2Display.SelectNormalArray = 'None'
    clip2Display.SelectTangentArray = 'None'
    clip2Display.OSPRayScaleArray = 'Magn'
    clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    clip2Display.SelectOrientationVectors = 'V Orientation'
    clip2Display.ScaleFactor = 1264.6288574218752
    clip2Display.SelectScaleArray = 'Magn'
    clip2Display.GlyphType = 'Arrow'
    clip2Display.GlyphTableIndexArray = 'Magn'
    clip2Display.GaussianRadius = 63.231442871093755
    clip2Display.SetScaleArray = ['POINTS', 'Magn']
    clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
    clip2Display.OpacityArray = ['POINTS', 'Magn']
    clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
    clip2Display.DataAxesGrid = 'GridAxesRepresentation'
    clip2Display.PolarAxes = 'PolarAxesRepresentation'
    clip2Display.ScalarOpacityFunction = anglePWF
    clip2Display.ScalarOpacityUnitDistance = 561.4769286441131
    clip2Display.OpacityArrayName = ['POINTS', 'Magn']
    clip2Display.SelectInputVectors = ['POINTS', 'V Orientation']
    clip2Display.WriteLog = ''
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    clip2Display.ScaleTransferFunction.Points = [3.967100565205328e-05, 0.0, 0.5, 0.0, 0.04559541866183281, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    clip2Display.OpacityTransferFunction.Points = [3.967100565205328e-05, 0.0, 0.5, 0.0, 0.04559541866183281, 1.0, 0.5, 0.0]
    
    # setup the color legend parameters for each legend in this view
    
    # get color legend/bar for temperatureanomalyLUT in view renderView1
    temperatureanomalyLUTColorBar = GetScalarBar(temperatureanomalyLUT, renderView1)
    temperatureanomalyLUTColorBar.WindowLocation = 'Any Location'
    temperatureanomalyLUTColorBar.Position = [0.11737445517790543, 0.44872706739811485]
    temperatureanomalyLUTColorBar.Title = 'temperature anomaly [C°]'
    temperatureanomalyLUTColorBar.ComponentTitle = ''
    temperatureanomalyLUTColorBar.HorizontalTitle = 1
    temperatureanomalyLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    temperatureanomalyLUTColorBar.LabelColor = [0.004364080262455177, 0.00434882124055848, 0.0043945983062485695]
    temperatureanomalyLUTColorBar.ScalarBarLength = 0.41687943262411353
    
    # set color bar visibility
    temperatureanomalyLUTColorBar.Visibility = 1
    
    # get color legend/bar for angleLUT in view renderView1
    angleLUTColorBar = GetScalarBar(angleLUT, renderView1)
    angleLUTColorBar.WindowLocation = 'Any Location'
    angleLUTColorBar.Position = [0.8279250146706206, 0.3427948053155604]
    angleLUTColorBar.Title = 'Movement'
    angleLUTColorBar.ComponentTitle = ''
    angleLUTColorBar.TitleJustification = 'Left'
    angleLUTColorBar.HorizontalTitle = 1
    angleLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    angleLUTColorBar.LabelColor = [0.9316700999465934, 0.927870603494316, 1.0]
    angleLUTColorBar.LabelFontSize = 1
    angleLUTColorBar.ScalarBarLength = 0.45193324374020116
    angleLUTColorBar.DataRangeLabelFormat = 'Up'
    
    # set color bar visibility
    angleLUTColorBar.Visibility = 1
    
    # show color legend
    clip1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    clip3Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    clip2Display.SetScalarBarVisibility(renderView1, True)
    
    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------
    
    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(text1)
    # ----------------------------------------------------------------
    WriteImage(f'/Users/macbook/OneDrive - UvA/{file}.png', renderView1,ImageResolution=[1784 ,728])    
    
    # ----------------------------------------------------------------
    # restore active source
    # ----------------------------------------------------------------
    ResetSession()


if __name__ == '__main__':
    SaveExtracts(ExtractsOutputDirectory='extracts')