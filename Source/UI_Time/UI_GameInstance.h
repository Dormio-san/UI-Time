// Currently nothing

#pragma once

#include "CoreMinimal.h"
#include "Engine/GameInstance.h"
#include "UI_GameInstance.generated.h"

/**
 * 
 */
UCLASS()
class UI_TIME_API UUI_GameInstance : public UGameInstance
{
	GENERATED_BODY()

public:
	// Override init and shutdown events to add our own functionality. 
	virtual void Init() override;
	virtual void Shutdown() override;

	// Init event to be called from blueprint
	UFUNCTION(BlueprintImplementableEvent, Category = "GameInstance")
	void Init_BP();

	// Shutdown event to be called from blueprint
	UFUNCTION(BlueprintImplementableEvent, Category = "GameInstance")
	void Shutdown_BP();
};
