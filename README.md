Pull games from chess.com to find the longest streak.
Print url, win chance and time for each game in the streak.

Very roughly estimates the longest expected streak (unless I messed up) with
ln(n)/ln(P) where n is total number of games and P is the avarage win chance.



# Usage

1. Download a chess.com user's games:

```bash
python getgames.py <ches.com username>
```

2. Find streak (when date is provided filter out all games prior to date):

```bash
python calc.py <chess.com username> <optional date string YYYYMMDD>
```

## Example (find longest streak of hikaru since 20th of Nov 2023):
```bash
python getgames.py hikaru
python calc.py hikaru 20231120
```
Output:
```
..........url.............................win chance.........time......
https://www.chess.com/game/live/94493554773 86.39% 11/23/2023, 16:54:33
https://www.chess.com/game/live/94494072015 86.66% 11/23/2023, 16:58:11
https://www.chess.com/game/live/94494142043 86.92% 11/23/2023, 17:03:22
https://www.chess.com/game/live/94499594489 94.29% 11/23/2023, 18:34:12
https://www.chess.com/game/live/94499660639 94.35% 11/23/2023, 18:38:24
https://www.chess.com/game/live/94500147353 94.41% 11/23/2023, 18:43:54
https://www.chess.com/game/live/94500255075 94.47% 11/23/2023, 18:47:59
https://www.chess.com/game/live/94500738999 94.53% 11/23/2023, 18:53:05
https://www.chess.com/game/live/94500839611 94.59% 11/23/2023, 18:58:44
https://www.chess.com/game/live/94501352031 94.65% 11/23/2023, 19:02:39
https://www.chess.com/game/live/94501428147 94.70% 11/23/2023, 19:07:10
https://www.chess.com/game/live/94501922135 94.76% 11/23/2023, 19:10:35
https://www.chess.com/game/live/94501989053 94.82% 11/23/2023, 19:16:13
https://www.chess.com/game/live/94502547173 94.88% 11/23/2023, 19:22:55
https://www.chess.com/game/live/94502633557 94.93% 11/23/2023, 19:28:04
https://www.chess.com/game/live/94503140211 94.99% 11/23/2023, 19:33:32
https://www.chess.com/game/live/94503245235 95.04% 11/23/2023, 19:38:32
https://www.chess.com/game/live/94503747963 95.09% 11/23/2023, 19:43:09
https://www.chess.com/game/live/94504353431 92.48% 11/23/2023, 19:50:48
https://www.chess.com/game/live/94504391535 92.56% 11/23/2023, 19:55:36
https://www.chess.com/game/live/94504994877 87.93% 11/23/2023, 20:06:15
https://www.chess.com/game/live/94505534955 92.56% 11/23/2023, 20:12:03
https://www.chess.com/game/live/94505612217 92.64% 11/23/2023, 20:14:26
https://www.chess.com/game/live/94505657157 92.72% 11/23/2023, 20:18:23
https://www.chess.com/game/live/94506143817 92.80% 11/23/2023, 20:23:32
https://www.chess.com/game/live/94506239259 92.87% 11/23/2023, 20:30:00
https://www.chess.com/game/live/94506771737 92.95% 11/23/2023, 20:35:27
https://www.chess.com/game/live/94512221489 94.00% 11/23/2023, 22:07:47
https://www.chess.com/game/live/94512770047 95.04% 11/23/2023, 22:13:32
https://www.chess.com/game/live/94512822335 95.09% 11/23/2023, 22:15:16
https://www.chess.com/game/live/94513283935 95.15% 11/23/2023, 22:18:38
https://www.chess.com/game/live/94513340483 95.20% 11/23/2023, 22:23:32
https://www.chess.com/game/live/94513422299 95.25% 11/23/2023, 22:27:22
https://www.chess.com/game/live/94513918849 95.31% 11/23/2023, 22:29:07
https://www.chess.com/game/live/94513946331 95.36% 11/23/2023, 22:32:53
https://www.chess.com/game/live/94514007815 95.41% 11/23/2023, 22:38:32
https://www.chess.com/game/live/94514536287 95.46% 11/23/2023, 22:42:13
https://www.chess.com/game/live/94514596083 95.51% 11/23/2023, 22:48:04
https://www.chess.com/game/live/94515127195 95.56% 11/23/2023, 22:51:15
https://www.chess.com/game/live/94515178033 95.60% 11/23/2023, 22:53:58
https://www.chess.com/game/live/94515220695 95.65% 11/23/2023, 23:00:02
https://www.chess.com/game/live/94515756815 95.70% 11/23/2023, 23:02:01
https://www.chess.com/game/live/94515786139 95.75% 11/23/2023, 23:04:18
https://www.chess.com/game/live/94515821175 95.79% 11/23/2023, 23:09:25
https://www.chess.com/game/live/94577930069 91.99% 11/24/2023, 16:19:43

Longest streak: 45 Probabilty of the streak happening when it happend: 5.634%
.......................................................................

hikaru has played 52315  with an avarge win chance of 83.6%
From this the longest expcted streak would be:  60 (Roughly estimated with # of games and avg win chance)

Other streaks (games won, chance, date)
5 , 73.685% 11/21/2023, 17:06:21
6 , 45.165% 11/22/2023, 00:50:13
11 , 43.848% 11/22/2023, 18:08:44
13 , 69.011% 11/22/2023, 19:04:16
45 , 5.634% 11/23/2023, 16:54:33

```
