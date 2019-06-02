using System;
using System.Collections.Generic;
using System.Linq;
using GameLight.Graphics;
using GameLight.Input;
using GameLight.Scene;
using GameLight.Sound;

namespace Zelda
{
	public class InventoryScreen : GameSceneBase
	{
		private enum State
		{
			TransitionIn,
			TransitionOut,
			Normal
		}
		private const int deploySpeed = 6;
		private static readonly Image frame = new Image("Images/inventory.png");

		private PlayScene underlay;
		private State transitionState = State.TransitionIn;
		private int transitionCounter = -224;
		
		public InventoryScreen(PlayScene underlay)
		{
			this.underlay = underlay;
		}

		protected override void Initialize()
		{
			
		}

		protected override void ProcessInput(InputEvent[] events)
		{
			foreach (InputEvent e in events)
			{
				if (e.Type == EventType.KeyDown)
				{
					if (e.Key == Key.Enter)
					{
						this.transitionState = State.TransitionOut;
					}
				}
			}
		}

		protected override void Render(Image gameScreen)
		{
			this.underlay.PublicRender(gameScreen);
			gameScreen.Blit(frame, 0, this.transitionCounter);
		}

		protected override void Update(int gameCounter)
		{
			switch (this.transitionState)
			{
				case State.Normal:
					this.transitionCounter = 0;
					break;

				case State.TransitionIn:
					this.transitionCounter = System.Math.Min(0, this.transitionCounter + deploySpeed);
					if (this.transitionCounter == 0)
					{
						this.transitionState = State.Normal;
					}
					break;

				case State.TransitionOut:
					this.transitionCounter = System.Math.Max(-224, this.transitionCounter - deploySpeed);
					if (this.transitionCounter == -224)
					{
						this.SwitchToScene(this.underlay);
					}
					break;
			}

			this.underlay.SetAsInactiveUnderlay(this.transitionCounter);
		}
	}
}
