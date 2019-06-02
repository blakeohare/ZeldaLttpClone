using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda
{
	public static class TextRenderer
	{
		private static Dictionary<string, Image> overlayNumbers = new Dictionary<string, Image>();

		private static Dictionary<string, Image> cache = new Dictionary<string, Image>();

		static TextRenderer()
		{
			for (int i = 0; i < 10; ++i)
			{
				overlayNumbers[i.ToString()] = new Image("Images/Text/Overlay/" + i.ToString() + ".png");
			}
		}

		public static Image GetOverlayNumber(int number, int digits)
		{
			string key = "o_" + number.ToString() + "_" + digits.ToString();
			Image output;
			if (!cache.TryGetValue(key, out output))
			{
				int digitWidth = overlayNumbers["0"].Width + 1;
				int width = digitWidth * digits;
				int height = overlayNumbers["0"].Height;
				string numAsString = number.ToString();
				output = new Image(width, height);

				while (numAsString.Length < digits)
				{
					numAsString = "0" + numAsString;
				}

				for (int i = 0; i < numAsString.Length; ++i)
				{
					output.Blit(overlayNumbers[numAsString[i].ToString()], i * digitWidth, 0);
				}

				cache[key] = output;
			}
			return output;
		}

		public static void PurgeCache()
		{
			cache.Clear();
		}
	}
}
