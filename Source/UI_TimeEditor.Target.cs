// Currently nothing

using UnrealBuildTool;
using System.Collections.Generic;

public class UI_TimeEditorTarget : TargetRules
{
	public UI_TimeEditorTarget(TargetInfo Target) : base(Target)
	{
		Type = TargetType.Editor;
		DefaultBuildSettings = BuildSettingsVersion.V6;

		ExtraModuleNames.AddRange( new string[] { "UI_Time" } );
	}
}
