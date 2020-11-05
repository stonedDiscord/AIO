import struct

# taken from AIO python server code, it'll make my life easier.
def string_unpack(buf):
	unpacked = buf.split("\0")[0]
	gay = list(buf)
	for l in range(len(unpacked+"\0")):
		del gay[0]
	return "".join(gay), unpacked

def buffer_read(format, buffer):
	if format != "S":
		unpacked = struct.unpack_from(format, buffer)
		size = struct.calcsize(format)
		liss = list(buffer)
		for l in range(size):
			del liss[0]
		returnbuffer = "".join(liss)
		return returnbuffer, unpacked[0]
	else:
		return string_unpack(buffer)

def versionToInt(ver):
    v = ver.split(".")
    major = v[0]
    minor = v[1]
    if len(v) > 2:
        patch = v[2]
    else:
        patch = "0"
    
    try:
        return int(major+minor+patch)
    except:
        return int(major+minor+"0")

def versionToStr(ver):
    major = ver[1]
    minor = ver[0]
    if len(ver) > 2:
        patch = ver[2]
    else:
        return major+"."+minor
    
    return  major+"."+minor+"."+patch