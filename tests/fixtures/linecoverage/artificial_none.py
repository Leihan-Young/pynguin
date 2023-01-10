#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2023 Pynguin Contributors
#
#  SPDX-License-Identifier: LGPL-3.0-or-later
#
def explicit_return_none(x):
    return None


def empty_function(x):
    """"""


def pass_function(x):
    pass


def only_return_on_branch(x):
    if x:
        return None


def return_on_both_branches(x):
    if x:
        return None
    return None


def pass_on_both(x):
    if x:
        pass
    else:
        pass


def for_return(x):
    for y in x:
        return y
