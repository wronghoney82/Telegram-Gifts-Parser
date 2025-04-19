from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import *

add_bot_url = f"https://t.me/{from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import *

add_bot_url = f"https://t.me/{from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import *

add_bot_url = f"https://t.me/{@Pareserit_bot}?startchannel=true"

main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Поиск подарков", callback_data="gifts_search")
    ],
    [
        InlineKeyboardButton(text="🌐 Глобальный поиск", callback_data="global_search")
    ],
    [
        InlineKeyboardButton(text="📊 Общая статистика БД", callback_data="general_db_stats")
    ],
    [
        InlineKeyboardButton(text="📌 Информация", callback_data="info")
    ]
])

main_admin = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Поиск подарков", callback_data="gifts_search")
    ],
    [
        InlineKeyboardButton(text="🌐 Глобальный поиск", callback_data="global_search")
    ],
    [
        InlineKeyboardButton(text="📊 Общая статистика БД", callback_data="general_db_stats")
    ],
    [
        InlineKeyboardButton(text="📌 Информация", callback_data="info")
    ],
    [
        InlineKeyboardButton(text="🔧 Админ-панель", callback_data="admin_panel")
    ]
])

admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚀 Парсинг подарков", callback_data="parsing")
    ],
    [
        InlineKeyboardButton(text="🔄 Авто-парсинг", callback_data="auto_parsing")  
    ],
    [
        InlineKeyboardButton(text="📊 Прогресс парсинга", callback_data="progress_parsing")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

parsing = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🟢 Начать парсинг подарков", callback_data="start_gift_parsing")
    ],
    [
        InlineKeyboardButton(text="🛑 Завершить парсинг подарков", callback_data="stop_gift_parsing")
    ]
])

auto_parsing = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚀 Добавить бота в канал", url=add_bot_url)
    ],
    [
        InlineKeyboardButton(text="🟢 Начать авто-парсинг", callback_data="start_auto_parsing")
    ],
    [
        InlineKeyboardButton(text="🛑 Завершить авто-парсинг", callback_data="stop_auto_parsing")
    ]
])

gift_management = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎁 Добавить подарок", callback_data="add_gift")
    ],
    [
        InlineKeyboardButton(text="🎁 Удалить подарок", callback_data="delete_gift")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ Да", callback_data="yes"),
        InlineKeyboardButton(text="❌ Нет", callback_data="no")
    ]
])

gifts_list = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🌌 Astral Shard", callback_data="Astral Shard:AstralShard"),
        InlineKeyboardButton(text="🔯 B-Day Candle", callback_data="B-Day Candle:BDayCandle")
    ],
    [
        InlineKeyboardButton(text="🍓 Berry Box", callback_data="Berry Box:BerryBox"),
        InlineKeyboardButton(text="🧁 Bunny Muffin", callback_data="Bunny Muffin:BunnyMuffin")
    ],
    [
        InlineKeyboardButton(text="🍬 Candy Cane", callback_data="Candy Cane:CandyCane"),
        InlineKeyboardButton(text="🍪 Cookie Heart", callback_data="Cookie Heart:CookieHeart")
    ],
    [
        InlineKeyboardButton(text="🔮 Crystal Ball", callback_data="Crystal Ball:CrystalBall"),
        InlineKeyboardButton(text="📅 Desk Calendar", callback_data="Desk Calendar:DeskCalendar")
    ],
    [
        InlineKeyboardButton(text="💍 Diamond Ring", callback_data="Diamond Ring:DiamondRing"),
        InlineKeyboardButton(text="🧢 Durov’s Cap", callback_data="Durov’s Cap:DurovsCap")
    ],
    [
        InlineKeyboardButton(text="💀 Electric Skull", callback_data="Electric Skull:ElectricSkull"),
        InlineKeyboardButton(text="🔇 Eternal Candle", callback_data="Eternal Candle:EternalCandle")
    ],
    [
        InlineKeyboardButton(text="🌹 Eternal Rose", callback_data="Eternal Rose:EternalRose"),
        InlineKeyboardButton(text="👁️ Evil Eye", callback_data="Evil Eye:EvilEye")
    ],
    [
        InlineKeyboardButton(text="🧉 Flying Broom", callback_data="Flying Broom:FlyingBroom"),
        InlineKeyboardButton(text="🪑 Genie Lamp", callback_data="Genie Lamp:GenieLamp")
    ],
    [
        InlineKeyboardButton(text="🍪 Ginger Cookie", callback_data="Ginger Cookie:GingerCookie"),
        InlineKeyboardButton(text="⭐ Hanging Star", callback_data="Hanging Star:HangingStar")
    ],
    [
        InlineKeyboardButton(text="🪴 Hex Pot", callback_data="Hex Pot:HexPot"),
        InlineKeyboardButton(text="🍰 Homemade Cake", callback_data="Homemade Cake:HomemadeCake")
    ],
    [
        InlineKeyboardButton(text="🍭 Hypno Lollipop", callback_data="Hypno Lollipop:HypnoLollipop"),
        InlineKeyboardButton(text="💎 Ion Gem", callback_data="Ion Gem:IonGem")
    ],
    [
        InlineKeyboardButton(text="📦 Jack-in-the-Box", callback_data="Jack-in-the-Box:JackInTheBox"),
        InlineKeyboardButton(text="🐰 Jelly Bunny", callback_data="Jelly Bunny:JellyBunny")
    ],
    [
        InlineKeyboardButton(text="🎩 Jester Hat", callback_data="Jester Hat:JesterHat"),
        InlineKeyboardButton(text="🔔 Jingle Bells", callback_data="Jingle Bells:JingleBells")
    ],
    [
        InlineKeyboardButton(text="🐸 Kissed Frog", callback_data="Kissed Frog:KissedFrog"),
        InlineKeyboardButton(text="🍭 Lol Pop", callback_data="Lol Pop:LolPop")
    ],
    [
        InlineKeyboardButton(text="🎒 Loot Bag", callback_data="Loot Bag:LootBag"),
        InlineKeyboardButton(text="🕯️ Love Candle", callback_data="Love Candle:LoveCandle")
    ],
    [
        InlineKeyboardButton(text="💖 Love Potion", callback_data="Love Potion:LovePotion"),
        InlineKeyboardButton(text="🐍 Lunar Snake", callback_data="Lunar Snake:LunarSnake")
    ],
    [
        InlineKeyboardButton(text="🎃 Mad Pumpkin", callback_data="Mad Pumpkin:MadPumpkin"),
        InlineKeyboardButton(text="🍷 Magic Potion", callback_data="Magic Potion:MagicPotion")
    ],
    [
        InlineKeyboardButton(text="🏆 Mini Oscar", callback_data="Mini Oscar:MiniOscar"),
        InlineKeyboardButton(text="🐾 Neko Helmet", callback_data="Neko Helmet:NekoHelmet")
    ],
    [
        InlineKeyboardButton(text="🎇 Party Sparkler", callback_data="Party Sparkler:PartySparkler"),
        InlineKeyboardButton(text="💐 Perfume Bottle", callback_data="Perfume Bottle:PerfumeBottle")
    ],
    [
        InlineKeyboardButton(text="🐸 Plush Pepe", callback_data="Plush Pepe:PlushPepe"),
        InlineKeyboardButton(text="🍑 Precious Peach", callback_data="Precious Peach:PreciousPeach")
    ],
    [
        InlineKeyboardButton(text="🎶 Record Player", callback_data="Record Player:RecordPlayer"),
        InlineKeyboardButton(text="🌸 Sakura Flower", callback_data="Sakura Flower:SakuraFlower")
    ],
    [
        InlineKeyboardButton(text="🎅 Santa Hat", callback_data="Santa Hat:SantaHat"),
        InlineKeyboardButton(text="😺 Scared Cat", callback_data="Scared Cat:ScaredCat")
    ],
    [
        InlineKeyboardButton(text="🗣️ Sharp Tongue", callback_data="Sharp Tongue:SharpTongue"),
        InlineKeyboardButton(text="💍 Signet Ring", callback_data="Signet Ring:SignetRing")
    ],
    [
        InlineKeyboardButton(text="💀 Skull Flower", callback_data="Skull Flower:SkullFlower"),
        InlineKeyboardButton(text="🔔 Sleigh Bell", callback_data="Sleigh Bell:SleighBell")
    ],
    [
        InlineKeyboardButton(text="🌍 Snow Globe", callback_data="Snow Globe:SnowGlobe"),
        InlineKeyboardButton(text="🧤 Snow Mittens", callback_data="Snow Mittens:SnowMittens")
    ],
    [
        InlineKeyboardButton(text="🍷 Spiced Wine", callback_data="Spiced Wine:SpicedWine"),
        InlineKeyboardButton(text="🍄 Spy Agaric", callback_data="Spy Agaric:SpyAgaric")
    ],
    [
        InlineKeyboardButton(text="📓 Star Notepad", callback_data="Star Notepad:StarNotepad"),
        InlineKeyboardButton(text="⌚ Swiss Watch", callback_data="Swiss Watch:SwissWatch")
    ],
    [
        InlineKeyboardButton(text="🎮 Tama Gadget", callback_data="Tama Gadget:TamaGadget"),
        InlineKeyboardButton(text="🎩 Top Hat", callback_data="Top Hat:TopHat")
    ],
    [
        InlineKeyboardButton(text="🐻 Toy Bear", callback_data="Toy Bear:ToyBear"),
        InlineKeyboardButton(text="💔 Trapped Heart", callback_data="Trapped Heart:TrappedHeart")
    ],
    [
        InlineKeyboardButton(text="🚬 Vintage Cigar", callback_data="Vintage Cigar:VintageCigar"),
        InlineKeyboardButton(text="🪆 Voodoo Doll", callback_data="Voodoo Doll:VoodooDoll")
    ],
    [
        InlineKeyboardButton(text="🌲 Winter Wreath", callback_data="Winter Wreath:WinterWreath"),
        InlineKeyboardButton(text="🎩 Witch Hat", callback_data="Witch Hat:WitchHat")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

search_methods = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎁 Модель", callback_data="Модель 🎁"),
        InlineKeyboardButton(text="🖼️ Фон", callback_data="Фон 🖼️")
    ],
    [
        InlineKeyboardButton(text="🌈 Модель + Фон", callback_data="Модель + Фон 🌈")
    ],
    [
        InlineKeyboardButton(text="🎨 Узор", callback_data="Узор 🎨"),
        InlineKeyboardButton(text="🔢 Номер", callback_data="Номер 🔢")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

global_search_methods = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🖼️ Фон", callback_data="Фон 🖼️")
    ],
    [
        InlineKeyboardButton(text="🌈 Фон + Узор", callback_data="Фон + Узор 🌈")
    ],
    [
        InlineKeyboardButton(text="🎨 Узор", callback_data="Узор 🎨"),
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

info = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="👨‍💻 Разработчик", url="https://t.me/danbesy")
    ],
    [
        InlineKeyboardButton(text="📢 Telegram канал", url="https://t.me/Danbesy_Dev")
    ],
    [
        InlineKeyboardButton(text="💻 GitHub разработчика", url="https://github.com/Danbesy")
    ]
])

send_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="⚡ Без ссылки на пользователя", callback_data="no_owner")
    ],
    [
        InlineKeyboardButton(text="🔗 С ссылкой на пользователя", callback_data="with_owner")
    ]
])}?startchannel=true"

main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Поиск подарков", callback_data="gifts_search")
    ],
    [
        InlineKeyboardButton(text="🌐 Глобальный поиск", callback_data="global_search")
    ],
    [
        InlineKeyboardButton(text="📊 Общая статистика БД", callback_data="general_db_stats")
    ],
    [
        InlineKeyboardButton(text="📌 Информация", callback_data="info")
    ]
])

main_admin = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Поиск подарков", callback_data="gifts_search")
    ],
    [
        InlineKeyboardButton(text="🌐 Глобальный поиск", callback_data="global_search")
    ],
    [
        InlineKeyboardButton(text="📊 Общая статистика БД", callback_data="general_db_stats")
    ],
    [
        InlineKeyboardButton(text="📌 Информация", callback_data="info")
    ],
    [
        InlineKeyboardButton(text="🔧 Админ-панель", callback_data="admin_panel")
    ]
])

admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚀 Парсинг подарков", callback_data="parsing")
    ],
    [
        InlineKeyboardButton(text="🔄 Авто-парсинг", callback_data="auto_parsing")  
    ],
    [
        InlineKeyboardButton(text="📊 Прогресс парсинга", callback_data="progress_parsing")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

parsing = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🟢 Начать парсинг подарков", callback_data="start_gift_parsing")
    ],
    [
        InlineKeyboardButton(text="🛑 Завершить парсинг подарков", callback_data="stop_gift_parsing")
    ]
])

auto_parsing = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚀 Добавить бота в канал", url=add_bot_url)
    ],
    [
        InlineKeyboardButton(text="🟢 Начать авто-парсинг", callback_data="start_auto_parsing")
    ],
    [
        InlineKeyboardButton(text="🛑 Завершить авто-парсинг", callback_data="stop_auto_parsing")
    ]
])

gift_management = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎁 Добавить подарок", callback_data="add_gift")
    ],
    [
        InlineKeyboardButton(text="🎁 Удалить подарок", callback_data="delete_gift")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ Да", callback_data="yes"),
        InlineKeyboardButton(text="❌ Нет", callback_data="no")
    ]
])

gifts_list = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🌌 Astral Shard", callback_data="Astral Shard:AstralShard"),
        InlineKeyboardButton(text="🔯 B-Day Candle", callback_data="B-Day Candle:BDayCandle")
    ],
    [
        InlineKeyboardButton(text="🍓 Berry Box", callback_data="Berry Box:BerryBox"),
        InlineKeyboardButton(text="🧁 Bunny Muffin", callback_data="Bunny Muffin:BunnyMuffin")
    ],
    [
        InlineKeyboardButton(text="🍬 Candy Cane", callback_data="Candy Cane:CandyCane"),
        InlineKeyboardButton(text="🍪 Cookie Heart", callback_data="Cookie Heart:CookieHeart")
    ],
    [
        InlineKeyboardButton(text="🔮 Crystal Ball", callback_data="Crystal Ball:CrystalBall"),
        InlineKeyboardButton(text="📅 Desk Calendar", callback_data="Desk Calendar:DeskCalendar")
    ],
    [
        InlineKeyboardButton(text="💍 Diamond Ring", callback_data="Diamond Ring:DiamondRing"),
        InlineKeyboardButton(text="🧢 Durov’s Cap", callback_data="Durov’s Cap:DurovsCap")
    ],
    [
        InlineKeyboardButton(text="💀 Electric Skull", callback_data="Electric Skull:ElectricSkull"),
        InlineKeyboardButton(text="🔇 Eternal Candle", callback_data="Eternal Candle:EternalCandle")
    ],
    [
        InlineKeyboardButton(text="🌹 Eternal Rose", callback_data="Eternal Rose:EternalRose"),
        InlineKeyboardButton(text="👁️ Evil Eye", callback_data="Evil Eye:EvilEye")
    ],
    [
        InlineKeyboardButton(text="🧉 Flying Broom", callback_data="Flying Broom:FlyingBroom"),
        InlineKeyboardButton(text="🪑 Genie Lamp", callback_data="Genie Lamp:GenieLamp")
    ],
    [
        InlineKeyboardButton(text="🍪 Ginger Cookie", callback_data="Ginger Cookie:GingerCookie"),
        InlineKeyboardButton(text="⭐ Hanging Star", callback_data="Hanging Star:HangingStar")
    ],
    [
        InlineKeyboardButton(text="🪴 Hex Pot", callback_data="Hex Pot:HexPot"),
        InlineKeyboardButton(text="🍰 Homemade Cake", callback_data="Homemade Cake:HomemadeCake")
    ],
    [
        InlineKeyboardButton(text="🍭 Hypno Lollipop", callback_data="Hypno Lollipop:HypnoLollipop"),
        InlineKeyboardButton(text="💎 Ion Gem", callback_data="Ion Gem:IonGem")
    ],
    [
        InlineKeyboardButton(text="📦 Jack-in-the-Box", callback_data="Jack-in-the-Box:JackInTheBox"),
        InlineKeyboardButton(text="🐰 Jelly Bunny", callback_data="Jelly Bunny:JellyBunny")
    ],
    [
        InlineKeyboardButton(text="🎩 Jester Hat", callback_data="Jester Hat:JesterHat"),
        InlineKeyboardButton(text="🔔 Jingle Bells", callback_data="Jingle Bells:JingleBells")
    ],
    [
        InlineKeyboardButton(text="🐸 Kissed Frog", callback_data="Kissed Frog:KissedFrog"),
        InlineKeyboardButton(text="🍭 Lol Pop", callback_data="Lol Pop:LolPop")
    ],
    [
        InlineKeyboardButton(text="🎒 Loot Bag", callback_data="Loot Bag:LootBag"),
        InlineKeyboardButton(text="🕯️ Love Candle", callback_data="Love Candle:LoveCandle")
    ],
    [
        InlineKeyboardButton(text="💖 Love Potion", callback_data="Love Potion:LovePotion"),
        InlineKeyboardButton(text="🐍 Lunar Snake", callback_data="Lunar Snake:LunarSnake")
    ],
    [
        InlineKeyboardButton(text="🎃 Mad Pumpkin", callback_data="Mad Pumpkin:MadPumpkin"),
        InlineKeyboardButton(text="🍷 Magic Potion", callback_data="Magic Potion:MagicPotion")
    ],
    [
        InlineKeyboardButton(text="🏆 Mini Oscar", callback_data="Mini Oscar:MiniOscar"),
        InlineKeyboardButton(text="🐾 Neko Helmet", callback_data="Neko Helmet:NekoHelmet")
    ],
    [
        InlineKeyboardButton(text="🎇 Party Sparkler", callback_data="Party Sparkler:PartySparkler"),
        InlineKeyboardButton(text="💐 Perfume Bottle", callback_data="Perfume Bottle:PerfumeBottle")
    ],
    [
        InlineKeyboardButton(text="🐸 Plush Pepe", callback_data="Plush Pepe:PlushPepe"),
        InlineKeyboardButton(text="🍑 Precious Peach", callback_data="Precious Peach:PreciousPeach")
    ],
    [
        InlineKeyboardButton(text="🎶 Record Player", callback_data="Record Player:RecordPlayer"),
        InlineKeyboardButton(text="🌸 Sakura Flower", callback_data="Sakura Flower:SakuraFlower")
    ],
    [
        InlineKeyboardButton(text="🎅 Santa Hat", callback_data="Santa Hat:SantaHat"),
        InlineKeyboardButton(text="😺 Scared Cat", callback_data="Scared Cat:ScaredCat")
    ],
    [
        InlineKeyboardButton(text="🗣️ Sharp Tongue", callback_data="Sharp Tongue:SharpTongue"),
        InlineKeyboardButton(text="💍 Signet Ring", callback_data="Signet Ring:SignetRing")
    ],
    [
        InlineKeyboardButton(text="💀 Skull Flower", callback_data="Skull Flower:SkullFlower"),
        InlineKeyboardButton(text="🔔 Sleigh Bell", callback_data="Sleigh Bell:SleighBell")
    ],
    [
        InlineKeyboardButton(text="🌍 Snow Globe", callback_data="Snow Globe:SnowGlobe"),
        InlineKeyboardButton(text="🧤 Snow Mittens", callback_data="Snow Mittens:SnowMittens")
    ],
    [
        InlineKeyboardButton(text="🍷 Spiced Wine", callback_data="Spiced Wine:SpicedWine"),
        InlineKeyboardButton(text="🍄 Spy Agaric", callback_data="Spy Agaric:SpyAgaric")
    ],
    [
        InlineKeyboardButton(text="📓 Star Notepad", callback_data="Star Notepad:StarNotepad"),
        InlineKeyboardButton(text="⌚ Swiss Watch", callback_data="Swiss Watch:SwissWatch")
    ],
    [
        InlineKeyboardButton(text="🎮 Tama Gadget", callback_data="Tama Gadget:TamaGadget"),
        InlineKeyboardButton(text="🎩 Top Hat", callback_data="Top Hat:TopHat")
    ],
    [
        InlineKeyboardButton(text="🐻 Toy Bear", callback_data="Toy Bear:ToyBear"),
        InlineKeyboardButton(text="💔 Trapped Heart", callback_data="Trapped Heart:TrappedHeart")
    ],
    [
        InlineKeyboardButton(text="🚬 Vintage Cigar", callback_data="Vintage Cigar:VintageCigar"),
        InlineKeyboardButton(text="🪆 Voodoo Doll", callback_data="Voodoo Doll:VoodooDoll")
    ],
    [
        InlineKeyboardButton(text="🌲 Winter Wreath", callback_data="Winter Wreath:WinterWreath"),
        InlineKeyboardButton(text="🎩 Witch Hat", callback_data="Witch Hat:WitchHat")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

search_methods = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎁 Модель", callback_data="Модель 🎁"),
        InlineKeyboardButton(text="🖼️ Фон", callback_data="Фон 🖼️")
    ],
    [
        InlineKeyboardButton(text="🌈 Модель + Фон", callback_data="Модель + Фон 🌈")
    ],
    [
        InlineKeyboardButton(text="🎨 Узор", callback_data="Узор 🎨"),
        InlineKeyboardButton(text="🔢 Номер", callback_data="Номер 🔢")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

global_search_methods = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🖼️ Фон", callback_data="Фон 🖼️")
    ],
    [
        InlineKeyboardButton(text="🌈 Фон + Узор", callback_data="Фон + Узор 🌈")
    ],
    [
        InlineKeyboardButton(text="🎨 Узор", callback_data="Узор 🎨"),
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

info = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="👨‍💻 Разработчик", url="https://t.me/danbesy")
    ],
    [
        InlineKeyboardButton(text="📢 Telegram канал", url="https://t.me/Danbesy_Dev")
    ],
    [
        InlineKeyboardButton(text="💻 GitHub разработчика", url="https://github.com/Danbesy")
    ]
])

send_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="⚡ Без ссылки на пользователя", callback_data="no_owner")
    ],
    [
        InlineKeyboardButton(text="🔗 С ссылкой на пользователя", callback_data="with_owner")
    ]
])}?startchannel=true"

main = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Поиск подарков", callback_data="gifts_search")
    ],
    [
        InlineKeyboardButton(text="🌐 Глобальный поиск", callback_data="global_search")
    ],
    [
        InlineKeyboardButton(text="📊 Общая статистика БД", callback_data="general_db_stats")
    ],
    [
        InlineKeyboardButton(text="📌 Информация", callback_data="info")
    ]
])

main_admin = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔍 Поиск подарков", callback_data="gifts_search")
    ],
    [
        InlineKeyboardButton(text="🌐 Глобальный поиск", callback_data="global_search")
    ],
    [
        InlineKeyboardButton(text="📊 Общая статистика БД", callback_data="general_db_stats")
    ],
    [
        InlineKeyboardButton(text="📌 Информация", callback_data="info")
    ],
    [
        InlineKeyboardButton(text="🔧 Админ-панель", callback_data="admin_panel")
    ]
])

admin_panel = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚀 Парсинг подарков", callback_data="parsing")
    ],
    [
        InlineKeyboardButton(text="🔄 Авто-парсинг", callback_data="auto_parsing")  
    ],
    [
        InlineKeyboardButton(text="📊 Прогресс парсинга", callback_data="progress_parsing")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

parsing = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🟢 Начать парсинг подарков", callback_data="start_gift_parsing")
    ],
    [
        InlineKeyboardButton(text="🛑 Завершить парсинг подарков", callback_data="stop_gift_parsing")
    ]
])

auto_parsing = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🚀 Добавить бота в канал", url=add_bot_url)
    ],
    [
        InlineKeyboardButton(text="🟢 Начать авто-парсинг", callback_data="start_auto_parsing")
    ],
    [
        InlineKeyboardButton(text="🛑 Завершить авто-парсинг", callback_data="stop_auto_parsing")
    ]
])

gift_management = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎁 Добавить подарок", callback_data="add_gift")
    ],
    [
        InlineKeyboardButton(text="🎁 Удалить подарок", callback_data="delete_gift")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

yes_or_no = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="✅ Да", callback_data="yes"),
        InlineKeyboardButton(text="❌ Нет", callback_data="no")
    ]
])

gifts_list = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🌌 Astral Shard", callback_data="Astral Shard:AstralShard"),
        InlineKeyboardButton(text="🔯 B-Day Candle", callback_data="B-Day Candle:BDayCandle")
    ],
    [
        InlineKeyboardButton(text="🍓 Berry Box", callback_data="Berry Box:BerryBox"),
        InlineKeyboardButton(text="🧁 Bunny Muffin", callback_data="Bunny Muffin:BunnyMuffin")
    ],
    [
        InlineKeyboardButton(text="🍬 Candy Cane", callback_data="Candy Cane:CandyCane"),
        InlineKeyboardButton(text="🍪 Cookie Heart", callback_data="Cookie Heart:CookieHeart")
    ],
    [
        InlineKeyboardButton(text="🔮 Crystal Ball", callback_data="Crystal Ball:CrystalBall"),
        InlineKeyboardButton(text="📅 Desk Calendar", callback_data="Desk Calendar:DeskCalendar")
    ],
    [
        InlineKeyboardButton(text="💍 Diamond Ring", callback_data="Diamond Ring:DiamondRing"),
        InlineKeyboardButton(text="🧢 Durov’s Cap", callback_data="Durov’s Cap:DurovsCap")
    ],
    [
        InlineKeyboardButton(text="💀 Electric Skull", callback_data="Electric Skull:ElectricSkull"),
        InlineKeyboardButton(text="🔇 Eternal Candle", callback_data="Eternal Candle:EternalCandle")
    ],
    [
        InlineKeyboardButton(text="🌹 Eternal Rose", callback_data="Eternal Rose:EternalRose"),
        InlineKeyboardButton(text="👁️ Evil Eye", callback_data="Evil Eye:EvilEye")
    ],
    [
        InlineKeyboardButton(text="🧉 Flying Broom", callback_data="Flying Broom:FlyingBroom"),
        InlineKeyboardButton(text="🪑 Genie Lamp", callback_data="Genie Lamp:GenieLamp")
    ],
    [
        InlineKeyboardButton(text="🍪 Ginger Cookie", callback_data="Ginger Cookie:GingerCookie"),
        InlineKeyboardButton(text="⭐ Hanging Star", callback_data="Hanging Star:HangingStar")
    ],
    [
        InlineKeyboardButton(text="🪴 Hex Pot", callback_data="Hex Pot:HexPot"),
        InlineKeyboardButton(text="🍰 Homemade Cake", callback_data="Homemade Cake:HomemadeCake")
    ],
    [
        InlineKeyboardButton(text="🍭 Hypno Lollipop", callback_data="Hypno Lollipop:HypnoLollipop"),
        InlineKeyboardButton(text="💎 Ion Gem", callback_data="Ion Gem:IonGem")
    ],
    [
        InlineKeyboardButton(text="📦 Jack-in-the-Box", callback_data="Jack-in-the-Box:JackInTheBox"),
        InlineKeyboardButton(text="🐰 Jelly Bunny", callback_data="Jelly Bunny:JellyBunny")
    ],
    [
        InlineKeyboardButton(text="🎩 Jester Hat", callback_data="Jester Hat:JesterHat"),
        InlineKeyboardButton(text="🔔 Jingle Bells", callback_data="Jingle Bells:JingleBells")
    ],
    [
        InlineKeyboardButton(text="🐸 Kissed Frog", callback_data="Kissed Frog:KissedFrog"),
        InlineKeyboardButton(text="🍭 Lol Pop", callback_data="Lol Pop:LolPop")
    ],
    [
        InlineKeyboardButton(text="🎒 Loot Bag", callback_data="Loot Bag:LootBag"),
        InlineKeyboardButton(text="🕯️ Love Candle", callback_data="Love Candle:LoveCandle")
    ],
    [
        InlineKeyboardButton(text="💖 Love Potion", callback_data="Love Potion:LovePotion"),
        InlineKeyboardButton(text="🐍 Lunar Snake", callback_data="Lunar Snake:LunarSnake")
    ],
    [
        InlineKeyboardButton(text="🎃 Mad Pumpkin", callback_data="Mad Pumpkin:MadPumpkin"),
        InlineKeyboardButton(text="🍷 Magic Potion", callback_data="Magic Potion:MagicPotion")
    ],
    [
        InlineKeyboardButton(text="🏆 Mini Oscar", callback_data="Mini Oscar:MiniOscar"),
        InlineKeyboardButton(text="🐾 Neko Helmet", callback_data="Neko Helmet:NekoHelmet")
    ],
    [
        InlineKeyboardButton(text="🎇 Party Sparkler", callback_data="Party Sparkler:PartySparkler"),
        InlineKeyboardButton(text="💐 Perfume Bottle", callback_data="Perfume Bottle:PerfumeBottle")
    ],
    [
        InlineKeyboardButton(text="🐸 Plush Pepe", callback_data="Plush Pepe:PlushPepe"),
        InlineKeyboardButton(text="🍑 Precious Peach", callback_data="Precious Peach:PreciousPeach")
    ],
    [
        InlineKeyboardButton(text="🎶 Record Player", callback_data="Record Player:RecordPlayer"),
        InlineKeyboardButton(text="🌸 Sakura Flower", callback_data="Sakura Flower:SakuraFlower")
    ],
    [
        InlineKeyboardButton(text="🎅 Santa Hat", callback_data="Santa Hat:SantaHat"),
        InlineKeyboardButton(text="😺 Scared Cat", callback_data="Scared Cat:ScaredCat")
    ],
    [
        InlineKeyboardButton(text="🗣️ Sharp Tongue", callback_data="Sharp Tongue:SharpTongue"),
        InlineKeyboardButton(text="💍 Signet Ring", callback_data="Signet Ring:SignetRing")
    ],
    [
        InlineKeyboardButton(text="💀 Skull Flower", callback_data="Skull Flower:SkullFlower"),
        InlineKeyboardButton(text="🔔 Sleigh Bell", callback_data="Sleigh Bell:SleighBell")
    ],
    [
        InlineKeyboardButton(text="🌍 Snow Globe", callback_data="Snow Globe:SnowGlobe"),
        InlineKeyboardButton(text="🧤 Snow Mittens", callback_data="Snow Mittens:SnowMittens")
    ],
    [
        InlineKeyboardButton(text="🍷 Spiced Wine", callback_data="Spiced Wine:SpicedWine"),
        InlineKeyboardButton(text="🍄 Spy Agaric", callback_data="Spy Agaric:SpyAgaric")
    ],
    [
        InlineKeyboardButton(text="📓 Star Notepad", callback_data="Star Notepad:StarNotepad"),
        InlineKeyboardButton(text="⌚ Swiss Watch", callback_data="Swiss Watch:SwissWatch")
    ],
    [
        InlineKeyboardButton(text="🎮 Tama Gadget", callback_data="Tama Gadget:TamaGadget"),
        InlineKeyboardButton(text="🎩 Top Hat", callback_data="Top Hat:TopHat")
    ],
    [
        InlineKeyboardButton(text="🐻 Toy Bear", callback_data="Toy Bear:ToyBear"),
        InlineKeyboardButton(text="💔 Trapped Heart", callback_data="Trapped Heart:TrappedHeart")
    ],
    [
        InlineKeyboardButton(text="🚬 Vintage Cigar", callback_data="Vintage Cigar:VintageCigar"),
        InlineKeyboardButton(text="🪆 Voodoo Doll", callback_data="Voodoo Doll:VoodooDoll")
    ],
    [
        InlineKeyboardButton(text="🌲 Winter Wreath", callback_data="Winter Wreath:WinterWreath"),
        InlineKeyboardButton(text="🎩 Witch Hat", callback_data="Witch Hat:WitchHat")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

search_methods = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🎁 Модель", callback_data="Модель 🎁"),
        InlineKeyboardButton(text="🖼️ Фон", callback_data="Фон 🖼️")
    ],
    [
        InlineKeyboardButton(text="🌈 Модель + Фон", callback_data="Модель + Фон 🌈")
    ],
    [
        InlineKeyboardButton(text="🎨 Узор", callback_data="Узор 🎨"),
        InlineKeyboardButton(text="🔢 Номер", callback_data="Номер 🔢")
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

global_search_methods = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🖼️ Фон", callback_data="Фон 🖼️")
    ],
    [
        InlineKeyboardButton(text="🌈 Фон + Узор", callback_data="Фон + Узор 🌈")
    ],
    [
        InlineKeyboardButton(text="🎨 Узор", callback_data="Узор 🎨"),
    ],
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

back_to_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_menu")
    ]
])

info = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="👨‍💻 Разработчик", url="https://t.me/danbesy")
    ],
    [
        InlineKeyboardButton(text="📢 Telegram канал", url="https://t.me/Danbesy_Dev")
    ],
    [
        InlineKeyboardButton(text="💻 GitHub разработчика", url="https://github.com/Danbesy")
    ]
])

send_menu = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="⚡ Без ссылки на пользователя", callback_data="no_owner")
    ],
    [
        InlineKeyboardButton(text="🔗 С ссылкой на пользователя", callback_data="with_owner")
    ]
])
