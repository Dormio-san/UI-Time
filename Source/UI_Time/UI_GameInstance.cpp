// Currently nothing


#include "UI_GameInstance.h"

void UUI_GameInstance::Init()
{
	// Call base implementation
	Super::Init();

	// Call the blueprint event
	Init_BP();
}

void UUI_GameInstance::Shutdown()
{
	// Call the blueprint event
	Shutdown_BP();

	// Call base implementation
	Super::Shutdown();
}