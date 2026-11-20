# TODO: dowiedzieć się co w tym pliku ma być xdd

## Dataset Features
| Column Name | Description |
| :--- | :--- |
| `user_id` | Unique alphanumeric identifier for each participant. |
| `age` | Participant age in years (skewed toward 18-45 demographic). |
| `gender` | Self-reported gender identity. |
| `occupation_type` | Broad employment category influencing wake-up obligations. |
| `chronotype` | Biological circadian preference (Morning Lark, Intermediate, Night Owl). |
| `bedtime_phone_minutes` | Total minutes spent actively using a smartphone in bed before attempting sleep. |
| `primary_bedtime_app` | The most used application category during the bedtime phone session. |
| `screen_brightness_pct` | Device screen brightness setting as a percentage (10% to 100%). |
| `blue_light_filter_active` | Binary flag (1 = Active, 0 = Inactive) for screen warming filters. |
| `caffeine_post_5pm_mg` | Estimated milligrams of caffeine consumed after 5:00 PM. |
| `physical_activity_min` | Total minutes of intentional physical exercise earlier in the day. |
| `sleep_latency_min` | Estimated minutes required to fall asleep after putting the device away. |
| `total_sleep_hours` | Calculated total hours of sleep achieved before the morning alarm. |
| `deep_sleep_pct` | Estimated percentage of total sleep spent in slow-wave deep sleep. |
| `rem_sleep_pct` | Estimated percentage of total sleep spent in Rapid Eye Movement (REM) stage. |
| `morning_alarm_snoozes` | Number of times the participant hit snooze on their morning alarm. |
| `next_day_fatigue_score` | Continuous target variable tracking subjective fatigue on a 1.0 to 10.0 scale. |
| `sleep_debt_category` | Multi-class categorical target defining the severity of sleep deficit. |