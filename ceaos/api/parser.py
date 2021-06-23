"""This file contains parsers for requests that come over the ZeroMQ wire"""
import json
from ..objects import Farm, Environment, Bed
from ..sensors import Sensor


def parse(msg: str, farm: Farm):
    decoded = json.loads(msg)
    if 'action' not in decoded:
        raise ValueError("No action declared")
    if 'cea-addr' not in decoded:
        raise ValueError("No target object specified")
    target = find_target(decoded['cea-addr'])
    


def find_target(cea_addr, farm):
    # We start by trying to find the target object
    addr = cea_addr.split('.')
    c_ptr = addr.pop(0)

    if c_ptr != farm.name:
        raise ValueError('cea-addr farm "{}" not found'.format(c_ptr))
    c_ptr = addr.pop(0)
    c_obj = farm

    if addr:  # This loops until no components are left
        if isinstance(c_obj, Farm):
            # We look inside the environments:
            if c_ptr not in c_obj.environments:
                raise ValueError('cea-addr env "{}" not found'.format(c_ptr))
            else:
                c_obj = c_obj.environments[c_ptr]
                c_ptr = addr.pop(0)

        elif isinstance(c_obj, Environment):
            if c_ptr in c_obj.sensors:
                c_obj = c_obj.sensors[c_ptr]
                c_ptr = addr.pop(0)
            elif c_ptr in c_obj.actuators:
                c_obj = c_obj.actuators[c_ptr]
                c_ptr = addr.pop(0)
            elif c_ptr in c_obj.beds:
                c_obj = c_obj.beds[c_ptr]
                c_ptr = addr.pop(0)
            else:
                raise ValueError('cea-addr key: "{}" not found.'.format(c_ptr))

        elif isinstance(c_obj, Bed):
            if c_ptr in c_obj.sensors:
                c_obj = c_obj.sensors[c_ptr]
                c_ptr = addr.pop(0)
            elif c_ptr in c_obj.actuators:
                c_obj = c_obj.actuators[c_ptr]
                c_ptr = addr.pop(0)
            elif c_ptr in c_obj.plants:
                c_obj = c_obj.plants[c_ptr]
                c_ptr = addr.pop(0)
            else:
                raise ValueError('cea-addr key: "{}" not found.'.format(c_ptr))

        elif isinstance(c_obj, Sensor):
            raise ValueError('cea-addr key overspecified. At leaf node. Remaining components: {}'.format(addr))
    
    return c_obj

