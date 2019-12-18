using Microsoft.AspNetCore.Mvc;
using MLHackathonServer.Entity;

namespace MLHackathonServer.Web
{
    public class DbController : Controller
    {
        private MLDBContext _db;
        public MLDBContext Db => _db ?? (MLDBContext)HttpContext?.RequestServices.GetService(typeof(MLDBContext));
    }
}