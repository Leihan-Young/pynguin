#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2023 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
import pynguin.utils.statistics.statistics as stat
from pynguin.utils.statistics.runtimevariable import RuntimeVariable


def test_variables_generator():
    value_1 = 23.42
    value_2 = 42.23
    stat.track_output_variable(RuntimeVariable.TotalTime, value_1)
    stat.track_output_variable(RuntimeVariable.TotalTime, value_2)
    result = [v for _, v in stat.variables_generator]
    assert result in ([], [value_1, value_2])
