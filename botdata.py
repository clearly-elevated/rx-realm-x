from discord.ext import commands
from pymongo import MongoClient
import os

class d(): # GENERAL STUFF
    limit = 10000000000000000
    prefix = '}'
    client = commands.Bot(command_prefix=prefix)
    mclient = MongoClient(os.environ['BC_LINK'])
    community = ['579385116443541526', 'https://discord.gg/53mGEpb']
    support = ['598936343350870029', 'https://discord.gg/tS2cdkf']
    version = '2.6'
    color = 0x000000
    extensions = ['cogs.commands for everyone',
                  'cogs.commands for eg',
                  'cogs.commands for helpers',
                  'cogs.commands for administrators',
                  'cogs.edit message systems',
                  'cogs.join leave systems',
                  'cogs.message systems',
                  'cogs.reaction systems']
    tos = 601459240116420649
    rx_rules = 601459187339231282
    rxs_rules = 601748137127837696
    cmds = {
        '1' : { # everyone
            'help' : [['h'], 'Gives information about commands.', 'p?help [command/number]', 'p?help\np?help ping\np?help 1'],
            'ping' : [[], 'Used to check if the bot is lagging.', 'p?ping', 'p?ping'],
            'invite' : [['inv'], 'Gives you invite links for the X bots and servers.', 'p?invite', 'p?invite'],
            'community' : [['com'], 'Gives you the official invite link to the community server.', 'p?community', 'p?community'],
            'support' : [['sup'], 'Gives you the official invite link to the bot support server.', 'p?support', 'p?support'],
            'tos' : [[], 'Shows you the X bots\' TOS.', 'p?tos', 'p?tos'],
            'rules' : [[], 'Shows you the server rules.', 'p?rules', 'p?rules'],
            'story' : [[], 'Used to check or manage stories.', 'p?story <option> [text]', 'p?story list\np?story select Something\np?story topic New topic'],
            'bump' : [[], 'Gives you information about bumping the server', 'p?bump', 'p?bump'],
            'pm' : [[], 'Gives you the partnership message', 'p?pm', 'p?pm'],
            'mc' : [[], 'Used for stuff related to the minecraft SMP server.', 'p?mc [option]', 'p?mc renew\np?mc'],
            'messages' : [['msgs'], 'Shows the server activity.', 'p?messages [user]', 'p?messages\np?messages @Someone'],
            'partnerships' : [['partners'], 'Shows the partnership activity.', 'p?partnerships [user]', 'p?partnerships\np?partnerships @Someone'],
            'upvotes' : [['uvs'], 'Shows the upvotes leaderboard.', 'p?upvotes [user]', 'p?upvotes\np?upvotes @Someone'],
            },
        '2' : { # partner managers
            '/' : [[], 'This category doesn\'t have any commands yet.', '/', '/'],
            },
        '3' : { # event/giveaway managers
            'event' : [[], 'Makes the events role mentionable/unmentionable.', 'p?event', 'p?event'],
            'giveaway' : [[], 'Makes the giveaways role mentionable/unmentionable.', 'p?giveaway', 'p?giveaway'],
            },
        '4' : { # helpers
            'update' : [[], 'Makes the updates role mentionable/unmentionable.', 'p?update', 'p?update'],
            'daily' : [[], 'Used to create new daily questions.', 'p?daily <question>', 'p?daily Insert cool question here?'],
            },
        '5' : { # moderators
            'This category doesn\'t have any commands yet.' : [[], '/', '/', '/'],
            },
        '6' : { # administrators
            'resetlb' : [['rlb'], 'Resets the partnerships and activity leaderboards.', 'p?resetlb', 'p?resetlb']
            },
        '7' : { # managers
            'This category doesn\'t have any commands yet.' : [[], '/', '/', '/'],
            },
        '8' : { # owners
            'This category doesn\'t have any commands yet.' : [[], '/', '/', '/'],
            },
        '9' : { # bot staff
            'This category doesn\'t have any commands yet.' : [[], '/', '/', '/'],
            },
        }

class c(): # CHANNELS
    rx_rules = 594445519556706342
    rxs_rules = 598938195358515200
    rx_logs = 594445327453388820
    rxs_logs = 598938868494106635
    rx_story = 594445691301003265
    rx_daily = 594445087841452040
    rx_confessions = 594445067498946570
    rx_vent = 594445636238311453
    rx_intros = 594445247585583104
    rx_general = 594446526990778378
    rxs_general = 598937814117253147
    rx_guestbook = 594445157282349057
    rxs_guestbook = 598938526435901470
    rx_partners = 600297591871373315
    rx_suggestions = 594445589349924876
    rxs_suggestions = 598938280175599627
    rx_partners = 600297591871373315
    rx_quotes = 594445460115292170

class r(): # ROLES
    rx_owners = 594447070514118666
    rx_managers = 594448592475783177
    rx_admins = 594448676449943554
    rx_mods = 594448734457298964
    rx_helpers = 594448787691274250
    rx_egs = 594448832352354314
    rx_pms = 599977519898427407
    rx_partners = 599969815255318540
    rx_updates = 594478648262656021
    rx_events = 594478805066711063
    rx_giveaways = 594478902886531076
    rx_daily = 594478950458327060
    rx_talk = 602138222864105473
    rx_mc_op = 600321330402820106
    rx_care = 594475752146206740
    rxs_updates = 599622878115397632
    rxs_xp = 599622878115397632
    rxs_xm = 599715578487504899
    rxs_xg = 599715624083783690
    rxs_staff = 598940056685641739
    rxs_owners = 599623049142206514

class e(): # EMOJIS
    worked = '<:rx1:585466467210887198>'
    error = '<:rx25:585466398244077569>'
    support = '<:rx4:585466465680097280>'
    ex = '<:rx24:585466398273437707>'
    check = '<:rx27:585466390991994880>'
    no_perms = '<:rx13:585466429331996673>'
    srt_right = '<:rx3:585466466443460609>'
    srt_left = '<:rx5:585466463901450245>'
    reload = '<:rx8:585466461284204545>'
    star = '<:rx6:585466463435882516>'
    ping_okay = '<:rx7:585466461712154634>'
    ping_bad = '<:rx9:585466458964754433>'
    ping_good = '<:rx11:585466458688192512>'
    off = '<:rx12:585466441646473236>'
    on = '<:rx10:585466458834731029>'
    n10 = '<:rx14:585466429097115669>'
    n9 = '<:rx15:585466427683766272>'
    n8 = '<:rx16:585466427662925834>'
    n7 = '<:rx17:585466425922027520>'
    n6 = '<:rx18:585466425544540190>'
    n5 = '<:rx20:585466423904567296>'
    n4 = '<:rx19:585466423934058536>'
    n3 = '<:rx23:585466421535047682>'
    n2 = '<:rx22:585466421845295115>'
    n1 = '<:rx21:585466421883043840>'
    upvote = '<:rx2:585466467047309322>'
    downvote = '<:rx26:585466398231232532>'
    blank = '<:rx28:585466390794862602>'
    log = '<:rx29:586175458035367936>'
    alogo = '<:rx30:587157500025896981>'
    mlogo = '<:rx31:587157529340018698>'
    flogo = '<:rx32:587157530338131974>'
    rlogo = '<:rx33:587157530577469450>'
    glogo = '<:rx34:587157532775022593>'
    plogo = '<:rx35:587157533974855690>'
    user = '<:rx36:587902710687203350>'
    server = '<:rx37:587902716676800512>'
    banned_user = '<:rx38:588078936790138892>'
    banned_server = '<:rx39:588078937146523689>'
    loading_discord = '<a:rx3a:585466398378033176>'
    loading_dots = '<a:rx2a:585466421652226050>'
    loading_circle = '<a:rx1a:585466421861941251>'
    minus = '<:rx40:595169579676860426>'
