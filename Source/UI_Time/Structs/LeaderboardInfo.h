// Nothing for now

#pragma once

#include "CoreMinimal.h"
#include "LeaderboardInfo.generated.h"

USTRUCT(BlueprintType)
struct FLeaderboardInfo : public FTableRowBase
{
	GENERATED_BODY();

	// Name
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Leaderboard Info")
	FText PlayerName;
	
	FLeaderboardInfo()
		: PlayerName(NSLOCTEXT("Leaderboard", "DefaultPlayerName", "You"))
	{}
	
	// Score
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Leaderboard Info")
	float Score = 0.0f;
	
	// Time
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Leaderboard Info")
	float Time = 0.0f;
};
