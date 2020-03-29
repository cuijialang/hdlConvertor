

import unittest
from tests.hdl_parse_tc import HdlParseTC, VERILOG
from hdlConvertor.to.basic_hdl_sim_model._main import ToBasicHdlSimModel
from hdlConvertor.translate.verilog_to_basic_hdl_sim_model import\
    verilog_to_basic_hdl_sim_model
from hdlConvertor.to.basic_hdl_sim_model.utils import discover_stm_outputs_context


def _to_basic_hdl_sim_model(context, language, buff):
    verilog_to_basic_hdl_sim_model(context)
    tv = ToBasicHdlSimModel(buff)
    stm_outputs = discover_stm_outputs_context(context)
    tv.print_HdlContext(context, stm_outputs)


class BasicHdlSimModelFromVerilogTC(HdlParseTC):

    def testSimpleSubunit(self):
        self.parseWithRef("simple_subunit.v", VERILOG,
                          lang_dir="basic_hdl_sim_model",
                          ref_fname="simple_subunit.py.txt",
                          to_hdl=_to_basic_hdl_sim_model)


if __name__ == '__main__':
    unittest.main()