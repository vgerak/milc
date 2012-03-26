
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x94\x91)\x00\xd0nt\xa5\x1b}\xd1\xdd_ \xe2\r'
    
_lr_action_items = {'Identifier':([0,],[1,]),'Let':([0,],[2,]),'$end':([1,2,3,],[-2,-1,0,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[3,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> Let','statement',1,'p_statement_let','lexer.py',128),
  ('statement -> Identifier','statement',1,'p_statement_identifier','lexer.py',132),
  ('expression -> Equals','expression',1,'p_expression_equals','lexer.py',136),
  ('expression -> Const_str','expression',1,'p_expression_const_str','lexer.py',140),
]
