from enum import Enum


class Command(Enum):
    """
    These are taken from the in-game manual of crawl.
    """

    #  Movement
    MOVE_OR_ATTACK_SW = 1
    MOVE_OR_ATTACK_S = 2
    MOVE_OR_ATTACK_SE = 3
    MOVE_OR_ATTACK_W = 4
    MOVE_OR_ATTACK_E = 5
    MOVE_OR_ATTACK_NW = 6
    MOVE_OR_ATTACK_N = 7
    MOVE_OR_ATTACK_NE = 8

    #  Rest
    REST_AND_LONG_WAIT = 9
    WAIT_1_TURN = 10

    #  Extended Movement
    AUTO_EXPLORE = 11
    INTERLEVEL_TRAVEL = 12
    FIND_ITEMS = 13
    SET_WAYPOINT = 14
    LONG_WALK_SW = 15
    LONG_WALK_S = 16
    LONG_WALK_SE = 17
    LONG_WALK_W = 18
    LONG_WALK_E = 19
    LONG_WALK_NW = 20
    LONG_WALK_N = 21
    LONG_WALK_NE = 22

    ATTACK_WITHOUT_MOVE_SW = 23
    ATTACK_WITHOUT_MOVE_S = 24
    ATTACK_WITHOUT_MOVE_SE = 25
    ATTACK_WITHOUT_MOVE_W = 26
    ATTACK_WITHOUT_MOVE_E = 27
    ATTACK_WITHOUT_MOVE_NW = 28
    ATTACK_WITHOUT_MOVE_N = 29
    ATTACK_WITHOUT_MOVE_NE = 30

    #  Autofight
    AUTO_FIGHT = 31
    AUTO_FIGHT_WITHOUT_MOVE = 32

    #  Item types (and common commands)
    WIELD_HAND_WEAPON = 33
    QUIVER_MISSILE = 34
    FIRE_MISSILE = 35
    SELECT_MISSILE_AND_FIRE = 36
    CYCLE_MISSILE_FORWARD = 37
    CYCLE_MISSILE_BACKWARD = 38
    WEAR_ARMOUR = 39
    TAKE_OFF_ARMOUR = 40
    CHOP_CORPSE = 41
    EAT = 42  # Note that later versions of crawl do not have an eat action
    READ = 43
    QUAFF = 44
    PUT_ON_JEWELLERY = 45
    REMOVE_JEWELLERY = 46
    EVOKE = 47
    SELECT_ITEM_TO_EVOKE = 48
    MEMORISE = 49
    COUNT_GOLD = 50

    #  Other gameplay actions
    USE_SPECIAL_ABILITY = 51
    CAST_SPELL_ABORT_WITHOUT_TARGETS = 52
    CAST_SPELL_NO_MATTER_WHAT = 53
    LIST_ALL_SPELLS = 54
    TELL_ALLIES = 55
    REDO_PREVIOUS_COMMAND = 56

    #  Game Saving and Quitting
    SAVE_GAME_AND_EXIT = 57
    SAVE_AND_EXIT_WITHOUT_QUERY = 58
    ABANDON_CURRENT_CHARACTER_AND_QUIT_GAME = 59

    #  Player Character Information
    DISPLAY_CHARACTER_STATUS = 60
    SHOW_SKILL_SCREEN = 61
    CHARACTER_OVERVIEW = 62
    SHOW_RELIGION_SCREEN = 63
    SHOW_ABILITIES_AND_MUTATIONS = 64
    SHOW_ITEM_KNOWLEDGE = 65
    SHOW_RUNES_COLLECTED = 66
    DISPLAY_WORN_ARMOUR = 67
    DISPLAY_WORN_JEWELLERY = 68
    DISPLAY_EXPERIENCE_INFO = 69

    #  Dungeon Interaction and Information
    OPEN_DOOR = 70
    CLOSE_DOOR = 71
    TRAVEL_STAIRCASE_DOWN = 72
    TRAVEL_STAIRCASE_UP = 73
    EXAMINE_CURRENT_TILE_PICKUP_PART_OF_SINGLE_STACK = 74
    EXAMINE_SURROUNDINGS_AND_TARGETS = 75
    EXAMINE_LEVEL_MAP = 76
    LIST_MONSTERS_ITEMS_FEATURES_IN_VIEW = 77
    TOGGLE_VIEW_LAYERS = 78
    SHOW_DUNGEON_OVERVIEW = 79
    TOGGLE_AUTO_PICKUP = 80
    SET_TRAVEL_SPEED_TO_CLOSEST_ALLY = 81

    #  Item Interaction (Inventory)
    SHOW_INVENTORY_LIST = 82
    INSCRIBE_ITEM = 83

    # Item Interaction (floor)
    PICKUP_ITEM = 84
    SELECT_ITEM_FOR_PICKUP = 85
    DROP_ITEM = 86
    DROP_LAST_ITEMS_PICKED_UP = 87

    #  Additional Actions
    EXIT_MENU = 88
    SHOW_PREVIOUS_GAME_MESSAGES = 89
    RESPOND_YES_TO_PROMPT = 90
    RESPOND_NO_TO_PROMPT = 91
    ENTER_KEY = 92

    # Menu specific actions
    EXAMINE_TILE_IN_EXPLORE_MENU = 93
