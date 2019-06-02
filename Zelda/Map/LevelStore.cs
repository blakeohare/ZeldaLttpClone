using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda.Map
{
	public static class LevelStore
	{
		private static Dictionary<string, ProtoLevel> levels = new Dictionary<string, ProtoLevel>();

		public static Level GetLevel(string name)
		{
			ProtoLevel level;
			if (!levels.TryGetValue(name, out level))
			{
				level = new ProtoLevel(name);
				levels.Add(name, level);
			}
			return level.GenerateNewLevel();
		}
	}
}
