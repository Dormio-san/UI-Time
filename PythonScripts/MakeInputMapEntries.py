import os

# ===================== CONFIG =====================
# Keyboard base path
KBM_PATH = "/Game/Art/UI/InputIcons/KBM/Dark/"

# Gamepad base path  
GAMEPAD_PATH = "/Game/Art/UI/InputIcons/Gamepad/Xbox_Series/"

# Output file
OUTPUT_FILE = "InputIconMapEntries.txt"

# ==================================================

def generate_keyboard_entries():
    entries = []
    
    # Numbers 0-9
    for i in range(10):
        map_key = str(i).upper()
        asset_name = f"{map_key}_Key_Dark"
        path = f'{KBM_PATH}{asset_name}.{asset_name}'
        entries.append(f'    InputIconMap.Add(FName(TEXT("{map_key}")), TSoftObjectPtr<UTexture2D>(FSoftObjectPath(TEXT("{path}"))));')
        print(f"{map_key}: {asset_name}")
        
    # Numpad numbers 0-9
    for i in range(10):
        map_key = str(i).upper()
        asset_name = f"{map_key}_Key_Dark"
        path = f'{KBM_PATH}{asset_name}.{asset_name}'
        entries.append(f'    InputIconMap.Add(FName(TEXT("{map_key}")), TSoftObjectPtr<UTexture2D>(FSoftObjectPath(TEXT("{path}"))));')
        print(f"Num {map_key}: {asset_name}")
    
    # Letters A-Z
    for c in range(ord('A'), ord('Z')+1):
        map_key = chr(c).upper()
        asset_name = f"{map_key}_Key_Dark"
        path = f'{KBM_PATH}{asset_name}.{asset_name}'
        entries.append(f'    InputIconMap.Add(FName(TEXT("{map_key}")), TSoftObjectPtr<UTexture2D>(FSoftObjectPath(TEXT("{path}"))));')
        print(f"{map_key}: {asset_name}")
        
    ### More keys icons
    # Mark_Left_Key_Dark
    # Mark_Right_Key_Dark
    # Plus_Tall_Key_Dark
    # Print_Screen_Key_Dark
    # Question_Key_Dark
    # "Tilda_Key_Dark
    #"LEFT SHIFT": "Shift_Alt_Key_Dark"
    #"ENTER": "Enter_Alt_Key_Dark"
    #"ENTER": "Enter_Tall_Key_Dark"
    #"BACKSPACE": "Backspace_Alt_Key_Dark"
    
    ### Keys with no icons
    # "MOUSE WHEEL AXIS": ""
    # "MOUSE WHEEL UP": ""
    # "MOUSE WHEEL DOWN": ""
    # "PAUSE": ""
    # "SCROLL LOCK": "" 
    # "UNDERSCORE": ""
    # "`": ""   # (back tick / back quote)
    # "APOSTROPHE": ""
    # "LEFT PARANTHESES": ""
    # "RIGHT PARANTHESES": ""
    # "AMPERSAND": ""
    # "CARET": ""
    # "DOLLAR": ""
    # "EXCLAMATION": ""
    # "COLON": ""
    
    # All other keys not included thus far
    all_other_keys = {
        "SPACE BAR": "Space_Key_Dark",
        "ENTER": "Enter_Key_Dark", 
        "TAB": "Tab_Key_Dark",
        "BACKSPACE": "Backspace_Key_Dark",
        "LEFT": "Arrow_Left_Key_Dark",
        "RIGHT": "Arrow_Right_Key_Dark",
        "UP": "Arrow_Up_Key_Dark",
        "DOWN": "Arrow_Down_Key_Dark",
        "LEFT SHIFT": "Shift_Key_Dark",
        "RIGHT SHIFT": "Shift_Key_Dark",
        "LEFT CTRL": "Ctrl_Key_Dark",
        "RIGHT CTRL": "Ctrl_Key_Dark",
        "LEFT ALT": "Alt_Key_Dark",
        "RIGHT ALT": "Alt_Key_Dark",
        "ESCAPE": "Esc_Key_Dark",
        "LEFT CMD": "Win_Key_Dark",
        "RIGHT CMD": "Command_Key_Dark",
        "HOME": "Home_Key_Dark",
        "INSERT": "Insert_Key_Dark",
        "END": "End_Key_Dark",
        "LEFT BRACKET": "Bracket_Left_Key_Dark",
        "RIGHT BRACKET": "Bracket_Right_Key_Dark",
        "CAPS LOCK": "Caps_Lock_Key_Dark",
        "COMMA": "Comma_Key_Dark",
        "DELETE": "Del_Key_Dark",
        "EQUALS": "Equals_Key_Dark",
        "F1": "F1_Key_Dark",
        "F2": "F2_Key_Dark",
        "F3": "F3_Key_Dark",
        "F4": "F4_Key_Dark",
        "F5": "F5_Key_Dark",
        "F6": "F6_Key_Dark",
        "F7": "F7_Key_Dark",
        "F8": "F8_Key_Dark",
        "F9": "F9_Key_Dark",
        "F10": "F10_Key_Dark",
        "F11": "F11_Key_Dark",
        "F12": "F12_Key_Dark",
        "HYPHEN": "Minus_Key_Dark",
        "LEFT MOUSE BUTTON": "Mouse_Left_Key_Dark",
        "MIDDLE MOUSE BUTTON": "Mouse_Middle_Key_Dark",
        "RIGHT MOUSE BUTTON": "Mouse_Right_Key_Dark",
        "PAGE DOWN": "Page_Down_Key_Dark",
        "PAGE UP": "Page_Up_Key_Dark",
        "PERIOD": "Period_Key_Dark",
        "APOSTROPHE": "Quote_Key_Dark",
        "QUOTE": "Quote_Key_Dark",
        "SEMICOLON": "Semicolon_Key_Dark",
        "SLASH": "Ford_Slash_Key_Dark",
        "BACKSLASH": "Back_Slash_Key_Dark",
        "NUM LOCK": "Num_Lock_Key_Dark",
        "NUM *": "Asterisk_Key_Dark",
        "NUM +": "Plus_Key_Dark",
        "NUM -": "Minus_Key_Dark",
        "NUM .": "Period_Key_Dark",
        "NUM /": "Ford_Slash_Key_Dark",
        "ASTERISK": "Asterisk_Key_Dark"
    }
    
    for map_key, asset_name in all_other_keys.items():
        path = f'{KBM_PATH}{asset_name}.{asset_name}'
        entries.append(f'    InputIconMap.Add(FName(TEXT("{map_key}")), TSoftObjectPtr<UTexture2D>(FSoftObjectPath(TEXT("{path}"))));')
        print(f"{map_key}: {asset_name}")
    
    return entries

def generate_gamepad_entries():
    entries = []
    
    # Face buttons
    gamepad_inputs = {
        "GAMEPAD FACE BUTTON BOTTOM": "XboxSeriesX_A",
        "GAMEPAD FACE BUTTON RIGHT": "XboxSeriesX_B", 
        "GAMEPAD FACE BUTTON LEFT": "XboxSeriesX_X",
        "GAMEPAD FACE BUTTON TOP": "XboxSeriesX_Y",
        "GAMEPAD D-PAD UP": "XboxSeriesX_Dpad_Up",
        "GAMEPAD D-PAD DOWN": "XboxSeriesX_Dpad_Down",
        "GAMEPAD D-PAD LEFT": "XboxSeriesX_Dpad_Left",
        "GAMEPAD D-PAD RIGHT": "XboxSeriesX_Dpad_Right",
        "GAMEPAD LEFT SHOULDER": "XboxSeriesX_LB",
        "GAMEPAD RIGHT SHOULDER": "XboxSeriesX_RB", 
        "GAMEPAD LEFT TRIGGER AXIS": "XboxSeriesX_LT",
        "GAMEPAD RIGHT TRIGGER AXIS": "XboxSeriesX_RT",
        "GAMEPAD SPECIAL LEFT": "XboxSeriesX_View",
        "GAMEPAD SPECIAL RIGHT": "XboxSeriesX_Menu",
        "GAMEPAD LEFT THUMBSTICK BUTTON": "XboxSeriesX_Left_Stick_Click",
        "GAMEPAD RIGHT THUMBSTICK BUTTON": "XboxSeriesX_Right_Stick_Click",
        "GAMEPAD LEFT THUMBSTICK X-AXIS": "XboxSeriesX_Left_Stick",
        "GAMEPAD LEFT THUMBSTICK Y-AXIS": "XboxSeriesX_Left_Stick",
        "GAMEPAD LEFT THUMBSTICK 2D-AXIS": "XboxSeriesX_Left_Stick",
        "GAMEPAD RIGHT THUMBSTICK X-AXIS": "XboxSeriesX_Right_Stick",
        "GAMEPAD RIGHT THUMBSTICK Y-AXIS": "XboxSeriesX_Right_Stick",
        "GAMEPAD RIGHT THUMBSTICK 2D-AXIS": "XboxSeriesX_Right_Stick",
    }
    
    for map_key, asset_name in gamepad_inputs.items():
        path = f'{GAMEPAD_PATH}{asset_name}.{asset_name}'
        entries.append(f'    InputIconMap.Add(FName(TEXT("{map_key}")), TSoftObjectPtr<UTexture2D>(FSoftObjectPath(TEXT("{path}"))));')
        print(f"{map_key}: {asset_name}")
    
    return entries

def main():
    all_entries = []
    
    print("Generating keyboard entries...")
    all_entries.extend(generate_keyboard_entries())
    
    print("Generating gamepad entries...")
    all_entries.extend(generate_gamepad_entries())
    
    # Write to file
    with open(OUTPUT_FILE, 'w') as f:
        f.writelines(line + '\n' for line in all_entries)
    
    print(f"✅ Generated {len(all_entries)} key entries at → {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
