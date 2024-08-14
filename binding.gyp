{
  "targets": [
    {
      "target_name": "gueco_ns",
      "sources":[
        "src/gueco_ns.cc",
        "src/clips_environment.cc"
      ],
      "include_dirs": [
        "CLIPS"
      ],
      "dependencies": [
        "clips"
      ],
    },
    {
      "target_name": "clips",
      "type": "static_library",
      "sources":[
        "CLIPS/defins.c",
        "CLIPS/router.c",
        "CLIPS/textpro.c",
        "CLIPS/classfun.c",
        "CLIPS/parsefun.c",
        "CLIPS/factbin.c",
        "CLIPS/insmoddp.c",
        "CLIPS/tmpltfun.c",
        "CLIPS/prdctfun.c",
        "CLIPS/multifun.c",
        "CLIPS/scanner.c",
        "CLIPS/insquery.c",
        "CLIPS/factlhs.c",
        "CLIPS/pprint.c",
        "CLIPS/tmpltutl.c",
        "CLIPS/generate.c",
        "CLIPS/objrtmch.c",
        "CLIPS/genrcfun.c",
        "CLIPS/inscom.c",
        "CLIPS/sysdep.c",
        "CLIPS/userdata.c",
        "CLIPS/cstrnbin.c",
        "CLIPS/symbol.c",
        "CLIPS/factprt.c",
        "CLIPS/edstruct.c",
        "CLIPS/globldef.c",
        "CLIPS/dffctbsc.c",
        "CLIPS/exprnops.c",
        "CLIPS/argacces.c",
        "CLIPS/edbasic.c",
        "CLIPS/tmpltbin.c",
        "CLIPS/ruledef.c",
        "CLIPS/msgpass.c",
        "CLIPS/modulcmp.c",
        "CLIPS/objrtfnx.c",
        "CLIPS/dffnxcmp.c",
        "CLIPS/tmpltlhs.c",
        "CLIPS/dffctdef.c",
        "CLIPS/factcmp.c",
        "CLIPS/envrnmnt.c",
        "CLIPS/classini.c",
        "CLIPS/classpsr.c",
        "CLIPS/cstrncmp.c",
        "CLIPS/dffctbin.c",
        "CLIPS/globlbsc.c",
        "CLIPS/msgcom.c",
        "CLIPS/factcom.c",
        "CLIPS/default.c",
        "CLIPS/memalloc.c",
        "CLIPS/userfunctions.c",
        "CLIPS/objcmp.c",
        "CLIPS/rulecstr.c",
        "CLIPS/globlcom.c",
        "CLIPS/dfinsbin.c",
        "CLIPS/filertr.c",
        "CLIPS/exprnbin.c",
        "CLIPS/msgpsr.c",
        "CLIPS/proflfun.c",
        "CLIPS/genrccmp.c",
        "CLIPS/rulecmp.c",
        "CLIPS/dffnxpsr.c",
        "CLIPS/genrcbin.c",
        "CLIPS/globlpsr.c",
        "CLIPS/cstrnops.c",
        "CLIPS/moduldef.c",
        "CLIPS/prntutil.c",
        "CLIPS/retract.c",
        "CLIPS/iofun.c",
        "CLIPS/factmngr.c",
        "CLIPS/objrtgen.c",
        "CLIPS/dffctcmp.c",
        "CLIPS/insmult.c",
        "CLIPS/inherpsr.c",
        "CLIPS/commline.c",
        "CLIPS/modulutl.c",
        "CLIPS/classinf.c",
        "CLIPS/prcdrfun.c",
        "CLIPS/cstrnchk.c",
        "CLIPS/rulecom.c",
        "CLIPS/factrhs.c",
        "CLIPS/symblbin.c",
        "CLIPS/symblcmp.c",
        "CLIPS/constrnt.c",
        "CLIPS/expressn.c",
        "CLIPS/modulbsc.c",
        "CLIPS/classcom.c",
        "CLIPS/sortfun.c",
        "CLIPS/rulebld.c",
        "CLIPS/dffnxexe.c",
        "CLIPS/dffnxbin.c",
        "CLIPS/cstrccom.c",
        "CLIPS/factqpsr.c",
        "CLIPS/objrtbin.c",
        "CLIPS/emathfun.c",
        "CLIPS/insfile.c",
        "CLIPS/reorder.c",
        "CLIPS/cstrnutl.c",
        "CLIPS/factgen.c",
        "CLIPS/miscfun.c",
        "CLIPS/factmch.c",
        "CLIPS/factqury.c",
        "CLIPS/genrcexe.c",
        "CLIPS/genrcpsr.c",
        "CLIPS/extnfunc.c",
        "CLIPS/modulpsr.c",
        "CLIPS/modulbin.c",
        "CLIPS/factfun.c",
        "CLIPS/prccode.c",
        "CLIPS/analysis.c",
        "CLIPS/insfun.c",
        "CLIPS/ruledlt.c",
        "CLIPS/conscomp.c",
        "CLIPS/rulelhs.c",
        "CLIPS/agenda.c",
        "CLIPS/pattern.c",
        "CLIPS/strngrtr.c",
        "CLIPS/exprnpsr.c",
        "CLIPS/factbld.c",
        "CLIPS/multifld.c",
        "CLIPS/evaluatn.c",
        "CLIPS/dfinscmp.c",
        "CLIPS/tmpltpsr.c",
        "CLIPS/incrrset.c",
        "CLIPS/globlbin.c",
        "CLIPS/facthsh.c",
        "CLIPS/insmngr.c",
        "CLIPS/filecom.c",
        "CLIPS/constrct.c",
        "CLIPS/edmisc.c",
        "CLIPS/watch.c",
        "CLIPS/rulebsc.c",
        "CLIPS/inspsr.c",
        "CLIPS/bmathfun.c",
        "CLIPS/classexm.c",
        "CLIPS/rulepsr.c",
        "CLIPS/immthpsr.c",
        "CLIPS/objbin.c",
        "CLIPS/prcdrpsr.c",
        "CLIPS/tmpltcmp.c",
        "CLIPS/cstrcbin.c",
        "CLIPS/edterm.c",
        "CLIPS/strngfun.c",
        "CLIPS/clsltpsr.c",
        "CLIPS/cstrnpsr.c",
        "CLIPS/engine.c",
        "CLIPS/tmpltrhs.c",
        "CLIPS/tmpltbsc.c",
        "CLIPS/utility.c",
        "CLIPS/developr.c",
        "CLIPS/globlcmp.c",
        "CLIPS/objrtbld.c",
        "CLIPS/edmain.c",
        "CLIPS/drive.c",
        "CLIPS/rulebin.c",
        "CLIPS/bsave.c",
        "CLIPS/bload.c",
        "CLIPS/tmpltdef.c",
        "CLIPS/genrccom.c",
        "CLIPS/msgfun.c",
        "CLIPS/dffctpsr.c",
        "CLIPS/reteutil.c",
        "CLIPS/lgcldpnd.c",
        "CLIPS/dffnxfun.c",
        "CLIPS/insqypsr.c",
        "CLIPS/objrtcmp.c",
        "CLIPS/factrete.c",
        "CLIPS/cstrcpsr.c",
        "CLIPS/crstrtgy.c"
      ],
      "linkflags": [
        "lm",
        "lrt",
        "ltermcap",
        "lstdc++"
      ],
      "cflags": [
        "-Wno-write-strings",
        "-Wunused-result",
        "-Wmissing-field-initializers",
        "-x c++"
      ],
      "defines": [
        "ALLOW_ENVIRONMENT_GLOBALS",
        "EMACS_EDITOR=0"
      ],
      "conditions": [
        [
          'OS == "linux"',
          {
            "defines": [
              "LINUX"
            ]
          }
        ]
      ]
    }
  ]
}
