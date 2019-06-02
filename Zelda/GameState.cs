using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda
{
	public class GameState
	{
		public static GameState Instance { get; private set; }
		static GameState()
		{
			GameState.Instance = new GameState();
		}

		private Dictionary<string, int> intValues = new Dictionary<string, int>();
		private Dictionary<string, string> stringValues = new Dictionary<string, string>();
		public int GetIntValue(string key)
		{
			int value;
			if (intValues.TryGetValue(key, out value))
			{
				return value;
			}
			return 0;
		}

		public string GetStringValue(string key)
		{
			string value;
			if (stringValues.TryGetValue(key, out value))
			{
				return value;
			}
			return string.Empty;
		}

		public bool GetBoolValue(string key)
		{
			return this.GetIntValue(key) == 1;
		}

		public void SetValue(string key, int value)
		{
			this.intValues[key] = value;
		}

		public void SetValue(string key, string value)
		{
			this.stringValues[key] = value;
		}

		public void SetValue(string key, bool value)
		{
			this.intValues[key] = value ? 1 : 0;
		}

		public int Rupees
		{
			get { return this.GetIntValue("rupees"); }
			set { this.SetValue("rupees", this.EnsureRange(value, 0, 999)); }
		}

		// Each heart container counts as 2 life
		public int Life
		{
			get { return this.GetIntValue("life"); }
			set { this.SetValue("life", this.EnsureRange(value, 0, this.HeartContainers * 2)); }
		}

		public int HeartContainers
		{
			get { return this.GetIntValue("heart_containers"); }
			set { this.SetValue("heart_containers", value); }
		}

		public int Bombs
		{
			get { return this.GetIntValue("bombs"); }
			set { this.SetValue("bombs", this.EnsureRange(value, 0, this.MaxBombs)); }
		}

		public int MaxBombs
		{
			get { return this.GetIntValue("max_bombs"); }
			set { this.SetValue("max_bombs", value); }
		}

		public int Arrows
		{
			get { return this.GetIntValue("arrows"); }
			set { this.SetValue("arrows", this.EnsureRange(value, 0, this.MaxBombs)); }
		}

		public int MaxArrows
		{
			get { return this.GetIntValue("max_arrows"); }
			set { this.SetValue("max_arrows", value); }
		}

		public bool HasSilverArrows
		{
			get { return this.GetBoolValue("has_silver_arrows"); }
			set { this.SetValue("has_silver_arrows", value); }
		}

		private int EnsureRange(int value, int minimum, int maximum)
		{
			if (value < minimum) return minimum;
			if (value > maximum) return maximum;
			return value;
		}
	}
}
