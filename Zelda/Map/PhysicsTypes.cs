using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda.Map
{
	public enum PhysicsTypes
	{
		Ground,
		ShortBlocking,
		TallBlocking,
		Hole,
		Grass,
		Water,
		Ice,
		DiagonalNW,
		DiagonalNE,
		DiagonalSW,
		DiagonalSE,
		JumpDown
	}

}
