from _Generic.GenericScript import GenericScript
from _Framework.Capabilities import *
import Live
from config import *

def create_instance(c_instance):
    """ The generic script can be customised by using config.py."""
    generic_script = GenericScript(c_instance,
                         Live.MidiMap.MapMode.relative_binary_offset,
                         Live.MidiMap.MapMode.absolute, DEVICE_CONTROLS,
                         TRANSPORT_CONTROLS, VOLUME_CONTROLS, TRACKARM_CONTROLS,
                         BANK_CONTROLS, CONTROLLER_DESCRIPTION)
    generic_script._device_selection_follows_track_selection = True
    return generic_script

def get_capabilities():
    return {CONTROLLER_ID_KEY: controller_id(vendor_id=9999, product_ids=[9999], model_name='Axiom 49'),
            PORTS_KEY: [inport(props=[NOTES_CC, REMOTE, SCRIPT]), outport(props=[SCRIPT])]}
