from mcpi.minecraft import Minecraft

name = "Yourname"
# connect to minecraft
address = "MinecraftServerAddress"
mc = Minecraft.create(address)

# get the x,y,z (position)
entity_id = mc.getPlayerEntityId(name)
position = mc.entity.getPos()