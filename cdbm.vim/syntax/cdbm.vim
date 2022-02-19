if exists("b:current_syntax")
	finish
endif

syntax match cdbmKey "^[^ \t]\+"
highlight default link cdbmKey Keyword

syntax match cdbmComment "^#.*$"
highlight default link cdbmComment Comment

let b:current_syntax = "cdbm"
