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
	UUI_GameInstance();
	
	// Override init and shutdown events to add our own functionality. 
	virtual void Init() override;
	virtual void Shutdown() override;

	// Init event to be called from blueprint
	UFUNCTION(BlueprintImplementableEvent, Category = "GameInstance")
	void Init_BP();

	// Shutdown event to be called from blueprint
	UFUNCTION(BlueprintImplementableEvent, Category = "GameInstance")
	void Shutdown_BP();
	
	// Look up an input icon texture by key display name
    UFUNCTION(BlueprintCallable, Category = "Input Icons")
    UTexture2D* GetInputIconTexture(const FText& KeyDisplayName) const;

protected:
    // Map that contains KeyDisplayName and corresponding 2D texture path
    UPROPERTY()
    TMap<FName, TSoftObjectPtr<UTexture2D>> InputIconMap;

    // Helper to make the display name text into a key for lookup in the map
    FName MakeInputIconKey(const FText& KeyDisplayName) const;
};
