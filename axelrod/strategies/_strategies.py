from __future__ import absolute_import

from .alternator import Alternator
from .appeaser import Appeaser
from .averagecopier import AverageCopier, NiceAverageCopier
from .axelrod_tournaments import (
    Davis, Feld, Grofman, Joss, Shubik, Tullock, Champion, Eatherley, Tester)
from .backstabber import BackStabber, DoubleCrosser
from .calculator import Calculator
from .cooperator import Cooperator, TrickyCooperator
from .cycler import AntiCycler, CyclerCCD, CyclerCCCD, CyclerCCCCCD
from .defector import Defector, TrickyDefector
from .forgiver import Forgiver, ForgivingTitForTat
from .geller import Geller, GellerCooperator, GellerDefector
from .gobymajority import (
    GoByMajority, GoByMajority10, GoByMajority20, GoByMajority40,
    GoByMajority5)
from .grudger import Grudger, ForgetfulGrudger, OppositeGrudger, Aggravater
from .grumpy import Grumpy
from .hunter import (
    DefectorHunter, CooperatorHunter, AlternatorHunter, MathConstantHunter,
    RandomHunter)
from .inverse import Inverse
from .mathematicalconstants import Golden, Pi, e
from .memoryone import (
    WinStayLoseShift,GTFT, StochasticCooperator, StochasticWSLS, ZDGTFT2,
    ZDExtort2, SoftJoss, MemoryOnePlayer)
from .mindcontrol import MindController, MindWarper, MindBender
from .mindreader import MindReader, ProtectedMindReader, MirrorMindReader
from .oncebitten import OnceBitten, FoolMeOnce, ForgetfulFoolMeOnce, FoolMeForever
from .prober import Prober, Prober2, Prober3, HardProber
from .punisher import Punisher, InversePunisher
from .qlearner import RiskyQLearner, ArrogantQLearner, HesitantQLearner, CautiousQLearner
from .rand import Random
from .retaliate import (
    Retaliate, Retaliate2, Retaliate3, LimitedRetaliate, LimitedRetaliate2,
    LimitedRetaliate3)
from .titfortat import (
    TitForTat, TitFor2Tats, TwoTitsForTat, Bully, SneakyTitForTat,
    SuspiciousTitForTat, AntiTitForTat, HardTitForTat, HardTitFor2Tats)

from .team4 import Team4Bot

# Note: Meta* strategies are handled in .__init__.py

strategies = [
    TitForTat,
    Team4Bot,
    TitFor2Tats, TwoTitsForTat
]
