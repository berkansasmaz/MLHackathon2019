using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;

namespace MLHackathonServer.Web
{
	[Authorize]
    public class SecureController : Controller
    {
        
    }
}