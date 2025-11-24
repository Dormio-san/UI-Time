// Currently nothing

using UnrealBuildTool;
using System.Collections.Generic;

public class UI_TimeTarget : TargetRules
{
	public UI_TimeTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Game;
		DefaultBuildSettings = BuildSettingsVersion.V5;

		ExtraModuleNames.AddRange( new string[] { "UI_Time" } );
	}
}
