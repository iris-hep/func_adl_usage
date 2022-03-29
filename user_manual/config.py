# Contains all the code for making the various sections easier.

from func_adl_servicex_xaodr21 import SXDSAtlasxAODR21, calib_tools

ds_xaod = SXDSAtlasxAODR21("rucio://mc16_13TeV:mc16_13TeV.361106.PowhegPythia8EvtGen_AZNLOCTEQ6L1_Zee.deriv.DAOD_PHYS.e3601_e5984_s3126_r10201_r10210_p5001?files=20")
ds_xaod = calib_tools.query_update(ds_xaod, perform_overlap_removal=False)
