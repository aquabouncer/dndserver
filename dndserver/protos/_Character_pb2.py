# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: _Character.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)
from . import _Item_pb2 as __Item__pb2

_sym_db = _symbol_database.Default()





DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10_Character.proto\x12\tDC.Packet\x1a\x0b_Item.proto\"\x96\x02\n\x0fSCHARACTER_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12.\n\x08nickName\x18\x02 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x03 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\r\x12\r\n\x05level\x18\x06 \x01(\r\x12\x13\n\x0bserviceGrpc\x18\x07 \x01(\t\x12+\n\x11\x43haracterItemList\x18\x08 \x03(\x0b\x32\x10.DC.Packet.SItem\x12\x32\n\x18\x43haracterStorageItemList\x18\t \x03(\x0b\x32\x10.DC.Packet.SItem\"\xf8\x01\n\x16SCHARACTER_FRIEND_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12.\n\x08nickName\x18\x02 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x03 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\r\x12\r\n\x05level\x18\x06 \x01(\r\x12\x16\n\x0elocationStatus\x18\x07 \x01(\r\x12\x19\n\x11PartyMemeberCount\x18\x08 \x01(\r\x12\x1c\n\x14PartyMaxMemeberCount\x18\t \x01(\r\"\x9b\x02\n\x15SCHARACTER_PARTY_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12.\n\x08nickName\x18\x02 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x03 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\r\x12\r\n\x05level\x18\x06 \x01(\r\x12\x15\n\risPartyLeader\x18\x07 \x01(\r\x12\x0f\n\x07isReady\x18\x08 \x01(\r\x12\x10\n\x08isInGame\x18\t \x01(\r\x12\'\n\requipItemList\x18\n \x03(\x0b\x32\x10.DC.Packet.SItem\x12\x10\n\x08partyIdx\x18\x0b \x01(\r\"\xc1\x01\n\x15SCHARACTER_TRADE_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12.\n\x08nickName\x18\x02 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x03 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\r\x12\r\n\x05level\x18\x06 \x01(\r\x12\x19\n\x11\x63haracterLocation\x18\x07 \x01(\r\"a\n\x11SACCOUNT_NICKNAME\x12\x18\n\x10originalNickName\x18\x01 \x01(\t\x12\x1d\n\x15streamingModeNickName\x18\x02 \x01(\t\x12\x13\n\x0bkarmaRating\x18\x03 \x01(\x05\"\x92\x01\n\x10SBLOCK_CHARACTER\x12\x11\n\taccountId\x18\x01 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x02 \x01(\t\x12.\n\x08nickName\x18\x03 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\r\"\xaf\x01\n\x1eSCHARACTER_GATHERING_HALL_INFO\x12\x11\n\taccountId\x18\x01 \x01(\t\x12.\n\x08nickName\x18\x02 \x01(\x0b\x32\x1c.DC.Packet.SACCOUNT_NICKNAME\x12\x16\n\x0e\x63haracterClass\x18\x03 \x01(\t\x12\x13\n\x0b\x63haracterId\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\r\x12\r\n\x05level\x18\x06 \x01(\r*\x80\x01\n\x0f\x46riend_Location\x12\x18\n\x14\x46riend_Location_NONE\x10\x00\x12\x19\n\x15\x46riend_Location_LOBBY\x10\x01\x12\x1b\n\x17\x46riend_Location_DUNGEON\x10\x02\x12\x1b\n\x17\x46riend_Location_OFFLINE\x10\x03\x42$\n\x15\x63om.packets.characterB\tcharacterP\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_Character_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\025com.packets.characterB\tcharacterP\000'
  _globals['_FRIEND_LOCATION']._serialized_start=1485
  _globals['_FRIEND_LOCATION']._serialized_end=1613
  _globals['_SCHARACTER_INFO']._serialized_start=45
  _globals['_SCHARACTER_INFO']._serialized_end=323
  _globals['_SCHARACTER_FRIEND_INFO']._serialized_start=326
  _globals['_SCHARACTER_FRIEND_INFO']._serialized_end=574
  _globals['_SCHARACTER_PARTY_INFO']._serialized_start=577
  _globals['_SCHARACTER_PARTY_INFO']._serialized_end=860
  _globals['_SCHARACTER_TRADE_INFO']._serialized_start=863
  _globals['_SCHARACTER_TRADE_INFO']._serialized_end=1056
  _globals['_SACCOUNT_NICKNAME']._serialized_start=1058
  _globals['_SACCOUNT_NICKNAME']._serialized_end=1155
  _globals['_SBLOCK_CHARACTER']._serialized_start=1158
  _globals['_SBLOCK_CHARACTER']._serialized_end=1304
  _globals['_SCHARACTER_GATHERING_HALL_INFO']._serialized_start=1307
  _globals['_SCHARACTER_GATHERING_HALL_INFO']._serialized_end=1482
# @@protoc_insertion_point(module_scope)
