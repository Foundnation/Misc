# state file generated using paraview version 5.11.0-RC2
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
for file in os.listdir("/Users/macbook/OneDrive - UvA/mantle01/"):

    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1784, 1122]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.OrientationAxesVisibility = 0
    renderView1.CenterOfRotation = [-2632.4877835455604, 0.0, 0.0]
    renderView1.HiddenLineRemoval = 1
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [27524.318635989053, 0.0, 0.0]
    renderView1.CameraFocalPoint = [-8796.610636273152, 0.0, 0.0]
    renderView1.CameraViewUp = [0.0, 0.0, 1.0]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 9400.548231483104
    renderView1.UseColorPaletteForBackground = 0
    renderView1.Background = [0.9518883039597161, 1.0, 0.989547570000763]
    renderView1.BackEnd = 'OSPRay raycaster'
    renderView1.OSPRayMaterialLibrary = materialLibrary1
    
    # init the 'GridAxes3DActor' selected for 'AxesGrid'
    renderView1.AxesGrid.Visibility = 1
    renderView1.AxesGrid.YTitle = 'Y Axis [km]'
    renderView1.AxesGrid.ZTitle = 'Z Axis [km]'
    renderView1.AxesGrid.GridColor = [0.0, 0.0, 0.0]
    renderView1.AxesGrid.XAxisUseCustomLabels = 1
    renderView1.AxesGrid.XAxisLabels = [0.0]
    renderView1.AxesGrid.YAxisUseCustomLabels = 1
    renderView1.AxesGrid.YAxisLabels = [-3000.0, 3000.0, 0.0]
    renderView1.AxesGrid.ZAxisUseCustomLabels = 1
    renderView1.AxesGrid.ZAxisLabels = [-3000.0, 0.0, 3000.0]
    
    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------
    
    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView1)
    layout1.SetSize(1784, 1122)
    
    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView1)
    # ----------------------------------------------------------------
    
    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------
    spherical001nc = NetCDFReader(registrationName=f'{file}', FileName=[f'/Users/macbook/OneDrive - UvA/mantle01/{file}'])

    # create a new 'NetCDF Reader'
    spherical001nc.Dimensions = '(lat, r, lon)'
    
    # create a new 'Slice'
    slice1 = Slice(registrationName='Slice1', Input=spherical001nc)
    slice1.SliceType = 'Plane'
    slice1.HyperTreeGridSlicer = 'Plane'
    slice1.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [-0.12210887778564938, 0.0, 0.0]
    
    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice1.HyperTreeGridSlicer.Origin = [-0.12210887778564938, 0.0, 0.0]
    
    # create a new 'Clip'
    clip1 = Clip(registrationName='Clip1', Input=spherical001nc)
    clip1.ClipType = 'Plane'
    clip1.HyperTreeGridClipper = 'Plane'
    clip1.Scalars = ['CELLS', 'spin transition-induced density anomaly']
    clip1.Value = -18.203079223632812
    
    # init the 'Plane' selected for 'ClipType'
    clip1.ClipType.Origin = [15.028931844600576, 0.0, 0.0]
    
    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip1.HyperTreeGridClipper.Origin = [-0.12210887778564938, 0.0, 0.0]
    
    # create a new 'Clip'
    clip2 = Clip(registrationName='Clip2', Input=clip1)
    clip2.ClipType = 'Cylinder'
    clip2.HyperTreeGridClipper = 'Plane'
    clip2.Scalars = ['CELLS', 'spin transition-induced density anomaly']
    clip2.Value = 2.552886962890625
    clip2.Invert = 0
    
    # init the 'Cylinder' selected for 'ClipType'
    clip2.ClipType.Axis = [1.0, 0.0, 0.0]
    clip2.ClipType.Radius = 3578.152818065241
    
    # init the 'Plane' selected for 'HyperTreeGridClipper'
    clip2.HyperTreeGridClipper.Origin = [-3181.5930340777, 0.0, 0.0]
    
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from clip2
    clip2Display = Show(clip2, renderView1, 'UnstructuredGridRepresentation')
    
    # get 2D transfer function for 'temperatureanomaly'
    temperatureanomalyTF2D = GetTransferFunction2D('temperatureanomaly')
    
    # get color transfer function/color map for 'temperatureanomaly'
    temperatureanomalyLUT = GetColorTransferFunction('temperatureanomaly')
    temperatureanomalyLUT.TransferFunction2D = temperatureanomalyTF2D
    temperatureanomalyLUT.RGBPoints = [-1099.197509765625, 0.0, 0.0, 0.34902, -1030.3021697998047, 0.039216, 0.062745, 0.380392, -961.4068298339844, 0.062745, 0.117647, 0.411765, -892.5114898681641, 0.090196, 0.184314, 0.45098, -823.6161499023438, 0.12549, 0.262745, 0.501961, -754.7208099365234, 0.160784, 0.337255, 0.541176, -685.8254699707031, 0.2, 0.396078, 0.568627, -616.9301300048828, 0.239216, 0.454902, 0.6, -548.0347900390625, 0.286275, 0.521569, 0.65098, -479.1394500732422, 0.337255, 0.592157, 0.701961, -410.2441101074219, 0.388235, 0.654902, 0.74902, -341.34877014160156, 0.466667, 0.737255, 0.819608, -272.45343017578125, 0.572549, 0.819608, 0.878431, -203.55809020996094, 0.654902, 0.866667, 0.909804, -134.66275024414062, 0.752941, 0.917647, 0.941176, -65.76741027832031, 0.823529, 0.956863, 0.968627, 3.1279296875, 0.988235, 0.960784, 0.901961, 3.1279296875, 0.941176, 0.984314, 0.988235, 47.220947265625, 0.988235, 0.945098, 0.85098, 91.31396484375, 0.980392, 0.898039, 0.784314, 140.91860961914062, 0.968627, 0.835294, 0.698039, 209.81394958496094, 0.94902, 0.733333, 0.588235, 278.70928955078125, 0.929412, 0.65098, 0.509804, 347.60462951660156, 0.909804, 0.564706, 0.435294, 416.4999694824219, 0.878431, 0.458824, 0.352941, 485.3953094482422, 0.839216, 0.388235, 0.286275, 554.2906494140625, 0.760784, 0.294118, 0.211765, 623.1859893798828, 0.701961, 0.211765, 0.168627, 692.0813293457031, 0.65098, 0.156863, 0.129412, 760.9766693115234, 0.6, 0.094118, 0.094118, 829.8720092773438, 0.54902, 0.066667, 0.098039, 898.7673492431641, 0.501961, 0.05098, 0.12549, 967.6626892089844, 0.45098, 0.054902, 0.172549, 1036.5580291748047, 0.4, 0.054902, 0.192157, 1105.453369140625, 0.34902, 0.070588, 0.211765]
    temperatureanomalyLUT.ColorSpace = 'Lab'
    temperatureanomalyLUT.NanColor = [0.25, 0.0, 0.0]
    temperatureanomalyLUT.ScalarRangeInitialized = 1.0
    
    # get opacity transfer function/opacity map for 'temperatureanomaly'
    temperatureanomalyPWF = GetOpacityTransferFunction('temperatureanomaly')
    temperatureanomalyPWF.Points = [-1099.197509765625, 0.0, 0.5, 0.0, 1105.453369140625, 1.0, 0.5, 0.0]
    temperatureanomalyPWF.ScalarRangeInitialized = 1
    
    # trace defaults for the display properties.
    clip2Display.Representation = 'Surface'
    clip2Display.ColorArrayName = ['CELLS', 'temperature anomaly']
    clip2Display.LookupTable = temperatureanomalyLUT
    clip2Display.SelectTCoordArray = 'None'
    clip2Display.SelectNormalArray = 'None'
    clip2Display.SelectTangentArray = 'None'
    clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    clip2Display.SelectOrientationVectors = 'None'
    clip2Display.ScaleFactor = 1105.58723053748
    clip2Display.SelectScaleArray = 'None'
    clip2Display.GlyphType = 'Arrow'
    clip2Display.GlyphTableIndexArray = 'None'
    clip2Display.GaussianRadius = 55.279361526874
    clip2Display.SetScaleArray = [None, '']
    clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
    clip2Display.OpacityArray = [None, '']
    clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
    clip2Display.DataAxesGrid = 'GridAxesRepresentation'
    clip2Display.PolarAxes = 'PolarAxesRepresentation'
    clip2Display.ScalarOpacityFunction = temperatureanomalyPWF
    clip2Display.ScalarOpacityUnitDistance = 132.83207481513156
    clip2Display.OpacityArrayName = ['CELLS', 'spin transition-induced density anomaly']
    clip2Display.SelectInputVectors = [None, '']
    clip2Display.WriteLog = ''
    
    # setup the color legend parameters for each legend in this view
    
    # get color legend/bar for temperatureanomalyLUT in view renderView1
    temperatureanomalyLUTColorBar = GetScalarBar(temperatureanomalyLUT, renderView1)
    temperatureanomalyLUTColorBar.WindowLocation = 'Any Location'
    temperatureanomalyLUTColorBar.Position = [0.0925588565022422, 0.5929997724428261]
    temperatureanomalyLUTColorBar.Title = 'Temperature Anomaly [CÂ°]'
    temperatureanomalyLUTColorBar.ComponentTitle = ''
    temperatureanomalyLUTColorBar.HorizontalTitle = 1
    temperatureanomalyLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
    temperatureanomalyLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
    temperatureanomalyLUTColorBar.ScalarBarLength = 0.32999999999999996
    
    # set color bar visibility
    temperatureanomalyLUTColorBar.Visibility = 1
    
    # show color legend
    clip2Display.SetScalarBarVisibility(renderView1, True)
    
    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------
    
    # ----------------------------------------------------------------
    # restore active source
    SetActiveSource(spherical001nc)
# ----------------------------------------------------------------
    ResetSession()


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')